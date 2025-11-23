from django.db import models
from inscripciones.models import Inscripcion

METODOS = (
    ("tarjeta", "Tarjeta"),
    ("efectivo", "Efectivo"),
    ("transferencia", "Transferencia"),
)

class Pago(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=20, choices=METODOS)
    procesado = models.BooleanField(default=False)
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def procesar_pago(self):
        self.procesado = True
        self.save()

class Reembolso(models.Model):
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_reembolso = models.DateTimeField(auto_now_add=True)
