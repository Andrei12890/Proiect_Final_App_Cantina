from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from livrari.forms import LivrariForm
from livrari.models import Livrari


class CreateLivrariView(LoginRequiredMixin, CreateView):
    model = Livrari
    form_class = LivrariForm
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('livrari:lista_livrari')


class LivrariView(LoginRequiredMixin, ListView):
    model = Livrari
    template_name = 'livrari/livrari_index.html'


class UpdateLivrariView(UpdateView):
    model = Livrari
    form_class = LivrariForm
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('livrari:lista_livrari')


@login_required
def deactivate_livrari(request, pk):
    Livrari.objects.filter(id=pk).update(active=False)
    return redirect('livrari:lista_livrari')

@login_required
def activate_livrari(request, pk):
    Livrari.objects.filter(id=pk).update(active=True)
    return redirect('livrari:lista_livrari')
