from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=30,blank=True,null=True)
    apellido= models.CharField(max_length=30,blank=True,null=True)
    correo= models.CharField(max_length=30,blank=True,null=True)
    fechaNacimiento = models.DateField(blank=True,null=True)
    def __str__(self):
        return '%s' % (self.id)
