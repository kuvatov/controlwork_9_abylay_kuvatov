from django.urls import path

from webapp.views import PhotoListView, PhotoCreateView
from webapp.views.photo_detail import PhotoDetailView

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list'),
    path('photos/<int:pk>', PhotoDetailView.as_view(), name='photo_detail'),
    path('photos/create/', PhotoCreateView.as_view(), name='photo_create')
]
