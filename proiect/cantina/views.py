from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from cantina.models import Cantina


class CreateCantinaView(LoginRequiredMixin, CreateView):
    model = Cantina
    template_name = 'forms.html'
    fields = ['denumire_produs', 'cantitate', 'pret_studenti']

    def get_success_url(self):
        return reverse('cantina:lista_cantina')


class CantinaView(LoginRequiredMixin, ListView):
    model = Cantina
    template_name = 'cantina/cantina_index.html'


class UpdateCantinaView(LoginRequiredMixin, UpdateView):
    model = Cantina
    fields = ['denumire_produs', 'cantitate', 'pret_studenti']
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('cantina:lista_cantina')


def deactivate_cantina(request, pk):
    Cantina.objects.filter(id=pk).update(active=False)
    return redirect('cantina:lista_cantina')


def activate_cantina(request, pk):
    Cantina.objects.filter(id=pk).update(active=True)
    return redirect('cantina:lista_cantina')

