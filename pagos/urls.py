from django.urls import path
from . import views

urlpatterns = [
    path('realizar/<int:inscripcion_id>/', views.pago_form, name='pago_form'),
    path('historial/', views.historial_pagos, name='historial_pagos'),
    path('reembolso/<int:pago_id>/', views.reembolso, name='reembolso'),
]
