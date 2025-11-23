from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),  # ← ESTA LÍNEA ES CLAVE
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('<int:pk>/', views.detalle_usuario, name='detalle_usuario'),
    path('<int:pk>/editar/', views.editar_usuario, name='editar_usuario'),
    path('<int:pk>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),
    path('<int:pk>/cambiar-contrasena/', views.cambiar_contrasena, name='cambiar_contrasena'),  # ← AGREGA ESTA LÍNEA
    path('perfil/', views.perfil, name='perfil'),
]
