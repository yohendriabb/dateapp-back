from django.db import models
from django.contrib.auth.models import User 

class Specialties(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="specialties")
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'

class Doctor(models.Model):
    specialities = models.ForeignKey(Specialties, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'

class Date(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    date_now = models.DateField()
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'