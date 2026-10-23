from django.contrib import admin
from .models import Acompanamiento, Nota, Sesion

admin.site.register(Sesion)
admin.site.register(Nota)
admin.site.register(Acompanamiento)