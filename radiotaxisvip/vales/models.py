from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class Vale(models.Model):
	usuario = models.ForeignKey(User)
	vehiculo = models.CharField(max_length=6)
	fecha_inicio = models.DateField()
	fecha_termino = models.DateField()
	#hora_inicio = models.TimeField()
	#hora_termino = models.TimeField()
	costo = models.PositiveIntegerField()
	distancia = models.PositiveIntegerField()
	en_espera = models.BooleanField()
	ESTADO = (
			('A','Aceptada'),
			('R','Rechazada'),
			('S','Sin observacion'),
		)
	estado = models.CharField(max_length=1,choices=ESTADO)
	class Meta:
		permissions = (
			("view_vale", "Can see available vales"),
			("accept_vale", "Can change status of vales"),
			("modify_vale", "Can modify the status of vales"),
			("close_vale", "Can remove a vale by setting its status as closed"),
		)


class ValeForm(ModelForm):
	class Meta:
		model = Vale
		fields = ['vehiculo','fecha_inicio']