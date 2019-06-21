from django import forms

from .models import Diagnostico,Paciente

class DiagnosticoForm(forms.ModelForm):

    class Meta:
        model = Diagnostico
        fields = (
            'medico',
            'paciente',
            'rut_entidad',
            'fecha',
            'fecha_entrega',
            'estado',
            )
class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = (
            'rut',
            'nombres',
            'apellido_paterno',
            'apellido_materno',
            'fecha_nacimiento',
            'ocupacion',
            'estado_civil',
            'direccion',
            'telefono',
            'prevision',
            )