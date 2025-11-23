from django.urls import path
from . import views

urlpatterns = [
    path('descargar/<int:certificado_id>/', views.descargar, name='descargar_certificado'),
    path('verificar/', views.verificar, name='verificar_certificado'),
]
