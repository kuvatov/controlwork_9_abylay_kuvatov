from django.urls import path

from webapp.views import PhotoListView, PhotoDetailView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list'),
    path('photos/<int:pk>', PhotoDetailView.as_view(), name='photo_detail'),
    path('photos/create/', PhotoCreateView.as_view(), name='photo_create'),
    path('photos/<int:pk>/update', PhotoUpdateView.as_view(), name='photo_update'),
    path('photos/<int:pk>/delete', PhotoDeleteView.as_view(), name='photo_delete')
]
