from django.db import models

class Diagnostico(models.Model):
    medico = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    paciente = models.ForeignKey('Paciente',default=1,on_delete=models.SET_DEFAULT)
    rut_entidad = models.CharField(max_length=200)
    fecha = models.DateField()
    fecha_entrega = models.DateField()
    ESTADO = (
        ('EN PROCESO','EN PROCESO'),
        ('DISPONIBLE','DISPONIBLE'),
    )
    estado = models.CharField(max_length=80,choices=ESTADO,default='DISPONIBLE')

class Paciente(models.Model):
    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    ocupacion = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    prevision = models.CharField(max_length=100)
    def __str__(self):
        return self.rut