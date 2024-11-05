from django import forms
from django.forms import TextInput, TimeInput

from livrari.models import Livrari
from cantina.models import Cantina


class LivrariForm(forms.ModelForm):
    class Meta:
        model = Livrari
        fields = '__all__'

        widgets = {
            'oras': TextInput(attrs={'placeholder': 'oras', 'class': 'form-control'}),
            'adresa': TextInput(attrs={'placeholder': 'adresa', 'class': 'form-control'}),
            'meniu': TextInput(attrs={'placeholder': 'meniu', 'class': 'form-control'}),
            'ora': TimeInput(attrs={'class': 'form-control', 'placeholder': 'HH:MM'}, format='%H:%M'),
            'pret': TextInput(attrs={'placeholder': 'pret', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(LivrariForm, self).__init__(*args, **kwargs)
        # self.pk = pk
