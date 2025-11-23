from django.urls import path
from . import views

urlpatterns = [
    path('inscribir/<int:evento_id>/', views.inscripcion_form, name='inscripcion_form'),
    path('mis/', views.mis_inscripciones, name='mis_inscripciones'),
    path('cancelar/<int:inscripcion_id>/', views.cancelar_inscripcion, name='cancelar_inscripcion'),
]
