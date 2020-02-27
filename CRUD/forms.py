from django import forms
from.models import Persona
class formularioPersona (forms.ModelForm):
    class Meta:
        model=Persona
        fields=[
            'nombre',
            'apellido',
            'correo',
            'fechaNacimiento',
        ]
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control' ,'id':'nombre'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'correo':forms.TextInput(attrs={'class':'form-control' }),
            'fechaNacimiento':forms.DateInput(attrs={'class':'form-control' }),
            
        }