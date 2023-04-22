from django.urls import path

from api.views import AddPhotoToFavouriteView, DeletePhotoFromFavouriteView

urlpatterns = [
    path('favourite/add/', AddPhotoToFavouriteView.as_view(), name='favourite_add'),
    path('favourite/delete/', DeletePhotoFromFavouriteView.as_view(), name='favourite_delete')
]