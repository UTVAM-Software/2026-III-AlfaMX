from academia.models import Actividad
from django.shortcuts import get_object_or_404, render


def realizar_actividad(request, actividad_id):
  actividad = get_object_or_404(Actividad, pk=actividad_id)
  return render(
      request, 'evaluarme/realizar_actividad.html', {'actividad': actividad}
  )