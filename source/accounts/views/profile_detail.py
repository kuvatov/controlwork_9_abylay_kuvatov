from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'profile/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        # reviews = user.comments.all()
        # context['reviews'] = reviews
        return context
