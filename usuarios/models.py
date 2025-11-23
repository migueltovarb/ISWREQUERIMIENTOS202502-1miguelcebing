from django.contrib.auth.models import AbstractUser
from django.db import models

ROLES = (
    ('asistente', 'Asistente'),
    ('organizador', 'Organizador'),
    ('logistica', 'Personal de Logística'),
    ('administrador', 'Administrador'),
)

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=30, choices=ROLES)
    
    def editar_perfil(self, nombre=None, email=None):
        if nombre:
            self.nombre = nombre
        if email:
            self.email = email
        self.save()
