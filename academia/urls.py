from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Login y Logout
    path('login/', auth_views.LoginView.as_view(template_name='academia/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Módulos
    path('', views.home_view, name='home'),
    path('modulo/<int:pk>/', views.detalle_modulo, name='detalle_modulo'),
    path('modulo/crear/', views.crear_modulo, name='crear_modulo'),
    path('modulo/<int:pk>/editar/', views.editar_modulo, name='editar_modulo'),
    path('modulo/<int:pk>/eliminar/', views.eliminar_modulo, name='eliminar_modulo'),

    # Alumnos
    path('registrar-alumno/', views.registrar_alumno, name='registrar_alumno'),
    path('alumno/<int:pk>/editar/', views.editar_alumno, name='editar_alumno'),
    path('alumno/<int:pk>/eliminar/', views.eliminar_alumno, name='eliminar_alumno'),

    # Gestión de Usuarios y Grupos (Django Auth)
    path('usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/<int:pk>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),
    path('grupos/crear/', views.crear_grupo, name='crear_grupo'),
]