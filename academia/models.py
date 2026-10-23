from django.db import models
from django.urls import reverse


class Modulo(models.Model):
    nombre = models.CharField(max_length=100)
    orden = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('detalle_modulo', args=[str(self.pk)])

    @property
    def total_lecciones(self):
        return self.lecciones.count()


class Leccion(models.Model):
    modulo = models.ForeignKey(
        Modulo, related_name='lecciones', on_delete=models.CASCADE
    )
    titulo = models.CharField(max_length=200)
    nivel = models.IntegerField(default=1)
    orden = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.modulo.nombre} - {self.titulo}'

    @property
    def total_actividades(self):
        return self.actividades.count()


class Actividad(models.Model):
    leccion = models.ForeignKey(
        Leccion, related_name='actividades', on_delete=models.CASCADE
    )
    tipo = models.CharField(max_length=50)
    instruccion_audio = models.TextField()
    contenido = models.JSONField()
    orden = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.tipo} ({self.leccion.titulo})'


class Alumno(models.Model):
    nombre = models.CharField(max_length=150)
    edad = models.IntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} ({self.edad} años)'

    @property
    def categoria_edad(self):
        if self.edad >= 18:
            return 'Adulto'
        else:
            return 'Menor de edad'