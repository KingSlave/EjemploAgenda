from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Persona(models.Model):
    idPersona = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
