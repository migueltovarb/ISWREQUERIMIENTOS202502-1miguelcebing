from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'estado', 'cupos', 'organizador')
    search_fields = ('nombre', 'organizador__username', 'organizador__nombre')
    list_filter = ('estado',)
