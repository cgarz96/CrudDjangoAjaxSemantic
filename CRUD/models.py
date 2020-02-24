from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=30,blank=True,null=True)
    apellido= models.CharField(max_length=30,blank=True,null=True)
    edad = models.IntegerField(blank=True,null=True)