from django.db import models
from inscripciones.models import Inscripcion

class Certificado(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to="certificados/")
    codigo_verificacion = models.CharField(max_length=100, unique=True)
    fecha_generacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Certificado - {self.inscripcion.usuario.username}"
