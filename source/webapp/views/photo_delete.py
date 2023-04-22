from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from webapp.models import Photo


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'webapp.delete_photo'
    model = Photo
    template_name = 'photo/photo_delete.html'
    success_url = reverse_lazy('photo_list')

    def has_permission(self):
        photo = self.get_object()
        return super().has_permission() or photo.author == self.request.user
