from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Klausimas(models.Model):
    tekstas = models.TextField()
    uzduotas_vartotojas = models.ForeignKey(User, on_delete=models.CASCADE, related_name="klausimai")
    atsakymas = models.TextField(blank=True, null=True)
    atsake_vartotojas = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="atsakymai")