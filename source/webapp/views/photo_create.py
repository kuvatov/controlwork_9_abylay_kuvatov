from django.urls import reverse
from django.views.generic import CreateView

from webapp.models import Photo


class PhotoCreateView(CreateView):
    model = Photo
    template_name = 'photo/photo_create.html'
    fields = ['photo', 'signature']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('publication_detail', kwargs={'pk': self.object.pk})
