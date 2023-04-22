from django.urls import reverse
from django.views.generic import UpdateView

from webapp.models import Photo


class PhotoUpdateView(UpdateView):
    model = Photo
    template_name = 'photo/photo_update.html'

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})
