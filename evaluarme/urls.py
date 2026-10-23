from django.urls import path
from . import views

urlpatterns = [
    path(
        'actividad/<int:actividad_id>/',
        views.realizar_actividad,
        name='realizar_actividad',
    ),
]