from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from accounts.forms import CustomUserChangeForm


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'profile/profile_update.html'

    def get_success_url(self):
        return reverse_lazy('profile_detail', args=(self.object.id,))
