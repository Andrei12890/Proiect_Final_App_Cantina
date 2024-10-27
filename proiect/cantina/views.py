from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from cantina.forms import CantinaForm
from cantina.models import Cantina


class CreateCantinaView(LoginRequiredMixin, CreateView):
    model = Cantina
    template_name = 'forms.html'
    # fields = ['denumire_produs', 'cantitate', 'pret_studenti']
    form_class = CantinaForm

    def get_form_kwargs(self):
        data = super(CreateCantinaView, self).get_form_kwargs()
        data.update({'pk': None})
        return data

    def get_success_url(self):
        return reverse('cantina:lista_cantina')


class CantinaView(LoginRequiredMixin, ListView):
    model = Cantina
    template_name = 'cantina/cantina_index.html'


class UpdateCantinaView(LoginRequiredMixin, UpdateView):
    model = Cantina
    # fields = ['denumire_produs', 'cantitate', 'pret_studenti']
    form_class = CantinaForm
    template_name = 'forms.html'

    def get_form_kwargs(self):
        data = super(UpdateCantinaView, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})
        return data

    def get_success_url(self):
        return reverse('cantina:lista_cantina')


@login_required
def deactivate_cantina(request, pk):
    Cantina.objects.filter(id=pk).update(active=False)
    return redirect('cantina:lista_cantina')


@login_required
def activate_cantina(request, pk):
    Cantina.objects.filter(id=pk).update(active=True)
    return redirect('cantina:lista_cantina')
