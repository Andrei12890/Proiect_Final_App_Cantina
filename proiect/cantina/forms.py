from django import forms
from django.forms import TextInput

from cantina.models import Cantina


class CantinaForm(forms.ModelForm):

    class Meta:
        model = Cantina
        fields = ['denumire_produs', 'cantitate', 'pret_studenti']

        widgets = {
            'denumire_produs': TextInput(attrs={'class': 'form-control', 'placeholder': 'denumire_produs'}),
            'cantitate': TextInput(attrs={'class': 'form-control', 'placeholder': 'cantitate'}),
            'pret_studenti': TextInput(attrs={'class': 'form-control', 'placeholder': 'pret_studenti'})
        }

    def __init__(self, pk, *args, **kwargs):
        super(CantinaForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        denumire_produs_value = self.cleaned_data.get('denumire_produs')
        cantitate_value = self.cleaned_data.get('cantitate')
        pret_studenti_value = self.cleaned_data.get('pret_studenti')
        if self.pk:
            if Cantina.objects.filter(denumire_produs=denumire_produs_value, cantitate=cantitate_value,
                                      pret_studenti=pret_studenti_value).exclude(id=self.pk).exists():
                self._errors['denumire_produs'] = self.error_class(['Produsul, cantitatea și prețul deja există'])
        else:
            if Cantina.objects.filter(denumire_produs=denumire_produs_value, cantitate=cantitate_value,
                                      pret_studenti=pret_studenti_value).exists():
                self._errors['denumire_produs'] = self.error_class(['Produsul, cantitatea și prețul deja există'])
        return self.cleaned_data
