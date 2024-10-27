from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView

from livrari.models import Livrari


class CreateLivrariView(LoginRequiredMixin, CreateView):
    model = Livrari
    form_class = LivrariForm
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('livrari:lista_livrari')
