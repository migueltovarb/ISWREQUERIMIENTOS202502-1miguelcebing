from django.urls import path
from . import views

urlpatterns = [
    path('asistencia/', views.asistencia_report, name='asistencia_report'),
    path('finanzas/', views.finanzas_report, name='finanzas_report'),
]
