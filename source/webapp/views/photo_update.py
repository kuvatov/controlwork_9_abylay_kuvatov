from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from webapp.models import Photo


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'webapp.change_photo'
    model = Photo
    template_name = 'photo/photo_update.html'
    fields = ['photo', 'signature']

    def has_permission(self):
        photo = self.get_object()
        return super().has_permission() or photo.author == self.request.user

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})
