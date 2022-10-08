import uuid

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import filters, viewsets, status, response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework_simplejwt.tokens import RefreshToken

from api_yamdb.settings import EMAIL_FROM_DEFAULT
from .mixins import CreateDestroyListViewSet
from .permissions import (
    IsAuthorOrReadOnlyPermission,
    IsAdmin,
    IsAdminOrReadOnly,
    IsAdminModeratorOrReadOnly
)
from titles.models import (
    User,
    Category,
    Genre,
    Title,
    Review,
    Comment,
)
from .serializers import (
    UserSerializer,
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
    ReviewSerializer,
    CommentSerializer,
    RegistrationSerializer,
    AuthetificationSerializer,
)


@api_view(['POST'])
@permission_classes([AllowAny])
def send_confirmation_code(request):
    """View-функция url auth/signup/."""

    username = request.data.get('username')
    email = request.data.get('email')

    try:
        user = User.objects.get(username=username, email=email)

        confirmation_code = str(uuid.uuid4())
        user.confirmation_code = confirmation_code
        user.save()

        data = request.data

    except ObjectDoesNotExist:
        serializer = RegistrationSerializer(data=request.data)

        if not serializer.is_valid():
            # Данные некорректны
            return response.Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        username = serializer.validated_data.get('username')
        email = serializer.validated_data.get('email')
        confirmation_code = str(uuid.uuid4())

        User.objects.get_or_create(
            username=username,
            email=email,
            confirmation_code=confirmation_code,
        )
        data = serializer.data

    send_mail(
        username,
        confirmation_code,
        EMAIL_FROM_DEFAULT,
        (email,),
        fail_silently=False,
    )

    return response.Response(
        data,
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def get_token(request):
    """View-функция url auth/token/."""

    serializer = AuthetificationSerializer(data=request.data)
    if not serializer.is_valid():
        return response.Response(
            # Данные некорректны
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    username = serializer.validated_data.get('username')
    user = get_object_or_404(User, username=username)

    confirmation_code = serializer.validated_data.get('confirmation_code')
    if confirmation_code != str(user.confirmation_code):
        # Неверный код подтверждения
        return response.Response(
            serializer.data,
            status=status.HTTP_400_BAD_REQUEST,
        )

    return response.Response(
        {'token': str(RefreshToken.for_user(user).access_token)},
        status=status.HTTP_200_OK,
    )   


class UsersViewSet(viewsets.ModelViewSet):
    """Класс вьюсета модели User."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_fields = ('username',)

    @action(
        methods=('get', 'patch',),
        permission_classes=(IsAuthenticated,),
        detail=False,
    )
    def me(self, request):
        """Обработка своей учётной записи."""

        username = request.user.username
        user = get_object_or_404(User, username=username)

        if request.method == 'PATCH':
            serializer = UserSerializer(user, data=request.data, partial=True)
            if not serializer.is_valid():
                return response.Response(
                    # Данные некорректны
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST,
                )
            serializer.save(
                role=user.role,
                confirmation_code=user.confirmation_code,
            )

        serializer = UserSerializer(user)
        return response.Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class CategoryViewSet(CreateDestroyListViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(CreateDestroyListViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'genre', 'name', 'year',)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission, IsAdminModeratorOrReadOnly)

    def get_queryset(self):
        new_queryset = Review.objects.select_related('title',)
        return new_queryset

    def perform_create(self, serializer):
        title = get_object_or_404(
            Title, pk=self.kwargs.get('title_id')
        )
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission, IsAdminModeratorOrReadOnly)

    def get_queryset(self):
        new_queryset = Comment.objects.select_related('review')
        return new_queryset

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review, pk=self.kwargs.get('review_id')
        )
        serializer.save(author=self.request.user, review=review)
