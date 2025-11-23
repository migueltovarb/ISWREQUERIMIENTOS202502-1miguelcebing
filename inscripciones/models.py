from django.db import models
from usuarios.models import Usuario
from eventos.models import Evento

class Inscripcion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    qr = models.CharField(max_length=255, blank=True)
    estado_pago = models.CharField(max_length=20, choices=[("pendiente", "Pendiente"), ("pagado", "Pagado")])
    estado = models.CharField(max_length=20, choices=[("inscrito", "Inscrito"), ("cancelado", "Cancelado")])
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    
    def cancelar(self):
        self.estado = "cancelado"
        self.save()
