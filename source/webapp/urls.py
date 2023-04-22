from django.urls import path

from webapp.views import PhotoListView

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list')
]
