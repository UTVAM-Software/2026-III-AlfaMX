from academia.models import Actividad
from django.contrib.auth.models import User
from django.db import models


class Intento(models.Model):
  usuario = models.ForeignKey(
      User, on_delete=models.CASCADE, related_name='intentos'
  )  #[cite: 21]
  actividad = models.ForeignKey(
      Actividad, on_delete=models.CASCADE, related_name='intentos'
  )  #[cite: 21]
  fecha_hora = models.DateTimeField(auto_now_add=True)  #[cite: 21]
  es_correcto = models.BooleanField(default=False)  #[cite: 21]
  puntaje = models.FloatField(default=0.0)  #[cite: 21]
  tiempo_seg = models.IntegerField(default=0)  #[cite: 21]
  usos_audio = models.IntegerField(default=0)  #[cite: 21]

  def __str__(self):
    return (
        f'Intento de {self.usuario.username} en Actividad {self.actividad.id}'
    )


class Trazo(models.Model):
  intento = models.ForeignKey(
      Intento, on_delete=models.CASCADE, related_name='trazos'
  )  #[cite: 21]
  caracter_objetivo = models.CharField(max_length=10)  #[cite: 21]
  coordenadas = models.JSONField()  # Secuencia x, y, t[cite: 21]
  precision = models.FloatField()  # Porcentaje de precisión[cite: 21]

  def __str__(self):
    return f'Trazo para {self.caracter_objetivo} - Precisión: {self.precision}%'