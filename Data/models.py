from django.db import models
from django.contrib.auth.models import User

# Create your models here.
gender_types = (
	("g1", "Masculino"), 
	("g2", "Femenino")
)

class Patient(models.Model):
	"""docstring for Patient"""
	patient_id = models.AutoField("Id", primary_key=True)
	create_at = models.DateTimeField("Fecha", auto_now=True)
	name = models.CharField("Nombre", max_length=50)
	first_name = models.CharField("Ap. Paterno", max_length=50, blank=True, null=True)
	last_name = models.CharField("Ap. Materno", max_length=50, blank=True, null=True)
	age = models.IntegetField("Edad")
	gender = models.CharField("Género", choices=gender_types, default=gender_types[0], max_length=2)
	phone = models.CharField("Teléfono", max_length=15, unique=True)
	address = models.CharField("Dirección", max_length=100)
	email = models.EmailField("E-mail", blank=True, null=True)
	status = models.BooleanField("Estado", default=True)
	user_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario", blank=True, null=True)

	class Meta:
		ordering = ["patient_id"]
		verbose_name_plural = "Pacientes"
		verbose_name = "Paciente"

	def __str__(self):
		return "{}".format(self.name)

class Medic(models.Model):
	"""docstring for Medic"""
	medic_id = models.AutoField("Id", primary_key=True)
	create_at = models.DateTimeField("Fecha", auto_now=True)
	name = models.CharField("Nombre", max_length=50)
	first_name = models.CharField("Ap. Paterno", max_length=50, blank=True, null=True)
	last_name = models.CharField("Ap. Materno", max_length=50, blank=True, null=True)
	age = models.IntegetField("Edad")
	gender = models.CharField("Género", choices=gender_types, default=gender_types[0], max_length=2)
	phone = models.CharField("Teléfono", max_length=15, unique=True)
	address = models.CharField("Dirección", max_length=100)
	email = models.EmailField("E-mail", blank=True, null=True)
	speciality = models.CharField("Especialidad", max_length=50)
	status = models.BooleanField("Estado", default=True)
	user_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario", blank=True, null=True)

	class Meta:
		ordering = ["medic_id"]
		verbose_name_plural = "Médicos"
		verbose_name = "Médico"

	def __str__(self):
		return "{}".format(self.name)

class GeoData(models.Model):
	"""docstring for GeoData"""
	geodata_id = models.AutoField("Id", primary_key=True)
	create_at = models.DateTimeField("Fecha", auto_now=True)
	latitude = models.FloatField("Latitud", default=0)
	longitude = models.FloatField("Longitud", default=0)
	patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Paciente")

	class Meta:
		verbose_name_plural = "GeoData"
		verbose_name = "GeoData"

	def __str__(self):
		return "{}".format(self.patient_id.name)

class Question(models.Model):
	"""docstring for Question"""
	question_id = models.AutoField("Id", primary_key=True)
	create_at = models.DateTimeField("Fecha", auto_now=True)
	question = models.CharField("Pregunta", max_length=100)
	score = models.IntegetField("Edad")
	status = models.BooleanField("Estado", default=True)
	
	class Meta:
		verbose_name_plural = "Preguntas"
		verbose_name = "Pregunta"

	def __str__(self):
		return "{}".format(self.patient_id.name)

class Pull(models.Model):
	"""docstring for Pull"""
	pull_id = models.AutoField("Id", primary_key=True)
	create_at = models.DateTimeField("Fecha", auto_now=True)
	diagnostic = models.CharField("Diagnóstico", max_length=100)
	status = models.BooleanField("Estado", default=True)
	geodata_id = models.ForeignKey(GeoData, on_delete=models.CASCADE, verbose_name="GeoData")
	patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Paciente")
	
	class Meta:
		verbose_name_plural = "Preguntas"
		verbose_name = "Pregunta"

	def __str__(self):
		return "{}".format(self.patient_id.name)

class Response(models.Model):
	"""docstring for Response"""
	response_id = models.AutoField("Id", primary_key=True)
	create_at = models.DateTimeField("Fecha", auto_now=True)
	response = models.BooleanField("Respuesta")
	value = models.CharField("Valor", max_length=50)
	status = models.BooleanField("Estado", default=True)
	pull_id = models.ForeignKey(Pull, on_delete=models.CASCADE, verbose_name="Encuesta")
	question_id = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Pregunta")

	class Meta:
		verbose_name_plural = "Respuestas"
		verbose_name = "Respuesta"

	def __str__(self):
		return "{}".format(self.patient_id.name)