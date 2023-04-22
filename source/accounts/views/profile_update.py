from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from accounts.forms import CustomUserChangeForm


class ProfileUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'accounts.change_user'
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'profile/profile_update.html'

    def has_permission(self):
        user = self.get_object()
        return super().has_permission() or user == self.request.user

    def get_success_url(self):
        return reverse_lazy('profile_detail', args=(self.object.id,))
