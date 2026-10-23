from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('modulo/<int:pk>/', views.detalle_modulo, name='detalle_modulo'),
    path('registro/', views.registrar_alumno, name='registrar_alumno'),
]