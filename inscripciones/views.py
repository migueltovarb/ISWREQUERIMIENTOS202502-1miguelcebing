from django.shortcuts import render, redirect, get_object_or_404
from .models import Inscripcion
from eventos.models import Evento

def inscripcion_form(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if request.method == "POST":
        inscripcion = Inscripcion.objects.create(
            usuario=request.user,
            evento=evento,
            estado_pago="pendiente",
            estado="inscrito"
        )
        return redirect("mis_inscripciones")
    return render(request, "inscripciones/inscripcion_form.html", {"evento": evento})

def mis_inscripciones(request):
    inscripciones = Inscripcion.objects.filter(usuario=request.user)
    return render(request, "inscripciones/mis_inscripciones.html", {"inscripciones": inscripciones})

def cancelar_inscripcion(request, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, pk=inscripcion_id)
    inscripcion.cancelar()
    return redirect("mis_inscripciones")
