from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from webapp.models import Photo


class PhotoDetailView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'
