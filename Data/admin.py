from django.contrib import admin

from Data.models import *

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Patient._meta.fields]

@admin.register(Medic)
class MedicAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Medic._meta.fields]

@admin.register(GeoData)
class GeoDataAdmin(admin.ModelAdmin):
	list_display = [field.name for field in GeoData._meta.fields]

@admin.register(Pull)
class PullAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Pull._meta.fields]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Question._meta.fields]

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Response._meta.fields]