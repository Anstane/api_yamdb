from xml.etree.ElementInclude import include
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UsersViewSet
from . import views

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r"users", UsersViewSet)
router_v1.register(r"users/<username>", UsersViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/token/', views.get_token, name='token'),
    path('v1/auth/signup/', views.send_comfirmation_code, name='confirm'),
]
