from django.contrib import admin
from .models import Actividad, Alumno, Leccion, Modulo


@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
  list_display = ('nombre', 'orden')
  search_fields = ('nombre',)


@admin.register(Leccion)
class LeccionAdmin(admin.ModelAdmin):
  list_display = ('titulo', 'modulo', 'nivel', 'orden')
  list_filter = ('modulo',)
  search_fields = ('titulo',)


@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
  list_display = ('tipo', 'leccion', 'orden')
  list_filter = ('leccion__modulo', 'tipo')


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
  list_display = ('nombre', 'edad', 'fecha_registro')
  search_fields = ('nombre',)