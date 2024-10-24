from django.db import models


class Cantina(models.Model):

    denumire_produs = models.CharField(max_length=100)
    cantitate = models.FloatField()
    pret_studenti = models.DecimalField(max_digits=6, decimal_places=2)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.denumire_produs} - {self.cantitate} - {self.pret_studenti} lei"
