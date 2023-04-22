from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


class ProfilePasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'profile/profile_password_change.html'
    success_url = reverse_lazy('photo_list')
