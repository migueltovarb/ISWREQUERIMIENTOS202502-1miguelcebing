from django.db import models
from usuarios.models import Usuario  # Usa tu modelo personalizado

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=20)
    cupos = models.PositiveIntegerField()
    organizador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="eventos_organizados")

    def actualizar_cupos(self, nuevocupo):
        self.cupos = nuevocupo
        self.save()

    def __str__(self):
        return self.nombre
