from django.views.generic import DetailView

from webapp.models import Photo


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'
