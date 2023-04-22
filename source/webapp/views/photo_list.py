from django.views.generic import ListView

from webapp.models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'
    context_object_name = 'photos'

    def get_queryset(self):
        return Photo.objects.exclude(is_deleted=True).order_by('-created_at')
