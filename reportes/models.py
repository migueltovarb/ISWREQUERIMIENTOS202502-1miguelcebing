from django.db import models
from eventos.models import Evento

class ReporteAsistencia(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    asistentes = models.PositiveIntegerField()
    generado_en = models.DateTimeField(auto_now_add=True)

class ReporteFinanciero(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    ingresos = models.DecimalField(max_digits=12, decimal_places=2)
    egresos = models.DecimalField(max_digits=12, decimal_places=2)
    generado_en = models.DateTimeField(auto_now_add=True)
