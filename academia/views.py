from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import get_object_or_404, redirect, render
from .models import Actividad, Alumno, Leccion, Modulo


# --- VISTAS DE MÓDULOS (LISTAR, DETALLE, CREAR, EDITAR, ELIMINAR) ---

@login_required
def home_view(request):
    modulos = Modulo.objects.all()
    alumnos = Alumno.objects.all()
    return render(request, 'academia/home.html', {
        'modulos': modulos,
        'alumnos': alumnos,
    })


@login_required
def detalle_modulo(request, pk):
    modulo = get_object_or_404(Modulo, pk=pk)
    lecciones = modulo.lecciones.all()
    return render(
        request,
        'academia/detalle_modulo.html',
        {'modulo': modulo, 'lecciones': lecciones},
    )


@login_required
@permission_required('academia.add_modulo', raise_exception=True)
def crear_modulo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        orden = request.POST.get('orden', 0)
        if nombre:
            Modulo.objects.create(nombre=nombre, orden=orden)
            return redirect('home')
    return render(request, 'academia/form_modulo.html')


@login_required
@permission_required('academia.change_modulo', raise_exception=True)
def editar_modulo(request, pk):
    modulo = get_object_or_404(Modulo, pk=pk)
    if request.method == 'POST':
        modulo.nombre = request.POST.get('nombre')
        modulo.orden = request.POST.get('orden', 0)
        modulo.save()
        return redirect('home')
    return render(request, 'academia/form_modulo.html', {'modulo': modulo})


@login_required
@permission_required('academia.delete_modulo', raise_exception=True)
def eliminar_modulo(request, pk):
    modulo = get_object_or_404(Modulo, pk=pk)
    if request.method == 'POST':
        modulo.delete()
        return redirect('home')
    return render(request, 'academia/eliminar_confirmar.html', {'objeto': modulo})


# --- VISTAS CRUD DE ALUMNOS ---

@login_required
def registrar_alumno(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
        if nombre and edad:
            Alumno.objects.create(nombre=nombre, edad=edad)
            return redirect('home')
    return render(request, 'academia/registrar_alumno.html')


@login_required
@permission_required('academia.change_alumno', raise_exception=True)
def editar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.nombre = request.POST.get('nombre')
        alumno.edad = request.POST.get('edad')
        alumno.save()
        return redirect('home')
    return render(request, 'academia/registrar_alumno.html', {'alumno': alumno})


@login_required
@permission_required('academia.delete_alumno', raise_exception=True)
def eliminar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        return redirect('home')
    return render(request, 'academia/eliminar_confirmar.html', {'objeto': alumno})


# --- GESTIÓN DE DJANGO AUTH (USUARIOS, GRUPOS Y PERMISOS) ---

@login_required
@permission_required('auth.view_user', raise_exception=True)
def gestion_usuarios(request):
    usuarios = User.objects.all()
    grupos = Group.objects.all()
    permisos = Permission.objects.all()
    return render(request, 'academia/gestion_usuarios.html', {
        'usuarios': usuarios,
        'grupos': grupos,
        'permisos': permisos,
    })


@login_required
@permission_required('auth.add_user', raise_exception=True)
def crear_usuario(request):
    grupos = Group.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        grupo_id = request.POST.get('grupo')
        if username and password:
            nuevo_usuario = User.objects.create_user(
                username=username, email=email, password=password
            )
            if grupo_id:
                grupo = Group.objects.get(pk=grupo_id)
                nuevo_usuario.groups.add(grupo)
            return redirect('gestion_usuarios')
    return render(request, 'academia/form_usuario.html', {'grupos': grupos})


@login_required
@permission_required('auth.delete_user', raise_exception=True)
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('gestion_usuarios')
    return render(request, 'academia/eliminar_confirmar.html', {'objeto': usuario})


@login_required
@permission_required('auth.add_group', raise_exception=True)
def crear_grupo(request):
    permisos = Permission.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        permisos_ids = request.POST.getlist('permisos')
        if nombre:
            grupo = Group.objects.create(name=nombre)
            for p_id in permisos_ids:
                permiso = Permission.objects.get(pk=p_id)
                grupo.permissions.add(permiso)
            return redirect('gestion_usuarios')
    return render(request, 'academia/form_grupo.html', {'permisos': permisos})