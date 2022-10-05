from django.urls import include, path

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views
from .views import UsersViewSet, CategoryViewSet, GenreViewSet, TitleViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
# router.register(r'users/<username>', UsersViewSet) - не совсем понял назначения этой строки
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', views.get_token, name='token'),
    path('v1/auth/signup/', views.send_comfirmation_code, name='confirm'),
]