from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Evento

@login_required
def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, "eventos/lista_eventos.html", {"eventos": eventos})

@login_required
def detalle_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, "eventos/detalle_evento.html", {"evento": evento})

@login_required
def crear_evento(request):
    # Solo organizador o admin pueden crear eventos
    if not (request.user.rol == "organizador" or request.user.rol == "administrador"):
        return HttpResponseForbidden("No tienes permiso para crear eventos.")
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        fecha = request.POST.get("fecha")
        estado = request.POST.get("estado")
        cupos = request.POST.get("cupos")
        Evento.objects.create(
            nombre=nombre,
            fecha=fecha,
            estado=estado,
            cupos=cupos,
            organizador=request.user
        )
        return redirect("lista_eventos")
    return render(request, "eventos/crear_evento.html")

@login_required
def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    # Solo administrador o el organizador dueño pueden editar
    if not (
        request.user.rol == "administrador"
        or (request.user.rol == "organizador" and evento.organizador_id == request.user.id)
    ):
        return HttpResponseForbidden("No tienes permiso para editar este evento.")
    if request.method == "POST":
        evento.nombre = request.POST.get("nombre")
        evento.fecha = request.POST.get("fecha")
        evento.estado = request.POST.get("estado")
        evento.cupos = request.POST.get("cupos")
        evento.save()
        return redirect("detalle_evento", pk=evento.pk)
    return render(request, "eventos/editar_evento.html", {"evento": evento})

@login_required
def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if not request.user.rol == "administrador":
        return HttpResponseForbidden("No tienes permiso para eliminar este evento.")
    if request.method == "POST":
        evento.delete()
        return redirect("lista_eventos")
    return render(request, "eventos/eliminar_evento.html", {"evento": evento})
