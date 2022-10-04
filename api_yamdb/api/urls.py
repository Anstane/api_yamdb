from django.urls import include, path
from rest_framework import routers

from .views import CategoryViewSet, GenreViewSet, TitleViewSet

router = routers.DefaultRouter()
router.register(r'v1/categories', CategoryViewSet)
router.register(r'v1/genres', GenreViewSet)
router.register(r'v1/titles', TitleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
