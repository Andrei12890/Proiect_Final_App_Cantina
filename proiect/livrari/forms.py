from django import forms

from livrari.models import Livrari


class LivrariForm(forms.ModelForm):
    class Meta:
        model = Livrari
        fields =
