from django.db import models
from cantina.models import Cantina


class Livrari(models.Model):

    oras = models.CharField(max_length=100)
    adresa = models.CharField(max_length=100)
    meniu = models.CharField(max_length=100)
    ora = models.TimeField(null=True, blank=True)
    pret = models.DecimalField(max_digits=6, decimal_places=2)
    # active = models.BooleanField(default=True)
    # created_at = models.DateTimeField(auto_now_add=True, blank=True)
    # updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.oras} {self.adresa} {self.meniu} {self.ora} {self.pret} lei"
