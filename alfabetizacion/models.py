from django.contrib.auth.models import User
from django.db import models


# 1. Catálogo dinámico para los Estados (adiós a los choices estáticos)
class Estado(models.Model):
  nombre = models.CharField(max_length=100, unique=True)
  descripcion = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.nombre


# 2. Escuela relacionada mediante ForeignKey al catálogo Estado
class Escuela(models.Model):
  nombre = models.CharField(max_length=150)
  tipo = models.CharField(max_length=50)
  estado = models.ForeignKey(
      Estado, on_delete=models.PROTECT, related_name='escuelas'
  )
  municipio = models.CharField(max_length=100)

  def __str__(self):
    return self.nombre


# 3. Perfil de usuario conectado al modelo oficial de Django (User)
class PerfilUsuario(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  rol = models.CharField(
      max_length=50
  )  # O puedes crear un catálogo de Roles si prefieres
  fecha_nacimiento = models.DateField(null=True, blank=True)
  fecha_registro = models.DateTimeField(auto_now_add=True)
  escuela = models.ForeignKey(
      Escuela, on_delete=models.SET_NULL, null=True, blank=True
  )

  def __str__(self):
    return self.user.username