from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters, mixins, viewsets, status, response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from .permissions import IsAuthorOrReadOnlyPermission
from titles.models import (
    User,
    Category,
    Genre,
    Title,
    Review,
    Comment
)
from .serializers import (
    UserSerializer,
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
    ReviewSerializer,
    CommentSerializer
)


@api_view(['POST'])
@permission_classes([AllowAny])
def send_confirmation_code(request):
    return response.Response(status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def get_token(request):
    return response.Response(status=status.HTTP_200_OK)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'genre', 'name', 'year',)


# Пока не знаю как реализовать permisson для администратора и модератора
class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def get_queryset(self):
        title = get_object_or_404(
            Title, pk=self.kwargs.get('title_id')
        )
        new_queryset = Review.objects.filter(title=title)
        return new_queryset

    def perform_create(self, serializer):
        title = get_object_or_404(
            Title, pk=self.kwargs.get('title_id')
        )
        serializer.save(author=self.request.user, title=title)


# Проблема аналогичная предыдущему вьюсету
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def get_queryset(self):
        review = get_object_or_404(
            Review, pk=self.kwargs.get('review_id')
        )
        new_queryset = Comment.objects.filter(review=review)
        return new_queryset

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review, pk=self.kwargs.get('review_id')
        )
        serializer.save(author=self.request.user, review=review)
