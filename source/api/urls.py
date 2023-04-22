from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views import PhotoViewSet, FavouriteViewSet

router = routers.DefaultRouter()
router.register(r'photos', PhotoViewSet)
router.register(r'favourites', FavouriteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth')
]
