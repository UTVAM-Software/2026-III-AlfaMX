from django.shortcuts import get_object_or_404, redirect, render
from .models import Actividad, Alumno, Leccion, Modulo


def home_view(request):
  modulos = Modulo.objects.all()
  return render(request, 'academia/home.html', {'modulos': modulos})


def detalle_modulo(request, pk):
  modulo = get_object_or_404(Modulo, pk=pk)
  lecciones = modulo.lecciones.all()
  return render(
      request,
      'academia/detalle_modulo.html',
      {'modulo': modulo, 'lecciones': lecciones},
  )


def registrar_alumno(request):
  if request.method == 'POST':
    nombre = request.POST.get('nombre')
    edad = request.POST.get('edad')
    if nombre and edad:
      Alumno.objects.create(nombre=nombre, edad=edad)
      return redirect('home')
  return render(request, 'academia/registrar_alumno.html')