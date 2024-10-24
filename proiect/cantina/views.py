from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from cantina.models import Cantina


class CreateCantinaView(CreateView):
    model = Cantina
    template_name = 'forms.html'
    fields = ['denumire_produs', 'cantitate', 'pret_studenti']

    def get_success_url(self):
        return reverse('cantina:adaugare')
