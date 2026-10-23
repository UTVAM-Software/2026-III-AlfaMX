# alumno/models.py
from django.contrib.auth.models import User
from django.db import models


class Sesion(models.Model):
  usuario = models.ForeignKey(
      User, on_delete=models.CASCADE, related_name='sesiones'
  )  #[cite: 21]
  fecha = models.DateField(auto_now_add=True)  #[cite: 21]
  minutos = models.IntegerField(default=0)  #[cite: 21]

  def __str__(self):
    return f'Sesión de {self.usuario.username} ({self.minutos} min)'


class Nota(models.Model):
  tutor = models.ForeignKey(
      User, on_delete=models.CASCADE, related_name='notas_redactadas'
  )  #[cite: 21]
  estudiante = models.ForeignKey(
      User, on_delete=models.CASCADE, related_name='notas_recibidas'
  )  #[cite: 21]
  texto = models.TextField()  #[cite: 21]
  necesita_apoyo = models.BooleanField(default=False)  
  fecha = models.DateField(auto_now_add=True)  #[cite: 21]

  def __str__(self):
    return f'Nota de {self.tutor.username} para {self.estudiante.username}'


class Acompanamiento(models.Model):
  tutor = models.ForeignKey(
      User, on_delete=models.CASCADE, related_name='estudiantes_asignados'
  )  #[cite: 21]
  estudiante = models.ForeignKey(
      User, on_delete=models.CASCADE, related_name='tutores_asignados'
  )  #[cite: 21]
  fecha_vinculo = models.DateField(auto_now_add=True)  #[cite: 21]
  estado = models.CharField(
      max_length=50, default='pendiente'
  )  # pendiente, activo, terminado[cite: 21]

  def __str__(self):
    return f'Tutor: {self.tutor.username} -> Estudiante: {self.estudiante.username}'