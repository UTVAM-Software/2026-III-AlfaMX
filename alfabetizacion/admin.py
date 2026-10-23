from django.contrib import admin
from .models import Escuela, Estado, PerfilUsuario


admin.site.register(Estado)
admin.site.register(Escuela)
admin.site.register(PerfilUsuario)