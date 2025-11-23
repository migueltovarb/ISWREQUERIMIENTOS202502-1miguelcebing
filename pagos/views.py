from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from decimal import Decimal, InvalidOperation
from .models import Pago, Reembolso
from inscripciones.models import Inscripcion

def pago_form(request, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, pk=inscripcion_id)
    if request.method == "POST":
        monto_raw = request.POST["monto"]
        metodo = request.POST["metodo"]
        error = None
        try:
            monto = Decimal(monto_raw)
            if monto <= 0 or monto > 999999.99:
                error = "Monto inválido. Debe ser positivo y razonable."
        except (InvalidOperation, ValueError):
            error = "Monto inválido. Escribe un número válido."
        if error:
            messages.error(request, error)
            return render(request, "pagos/pago_form.html", {"inscripcion": inscripcion})
        pago = Pago.objects.create(
            inscripcion=inscripcion,
            monto=monto,
            metodo=metodo
        )
        pago.procesar_pago()
        inscripcion.estado_pago = "pagado"
        inscripcion.save()
        return redirect("historial_pagos")
    return render(request, "pagos/pago_form.html", {"inscripcion": inscripcion})

def historial_pagos(request):
    pagos = Pago.objects.filter(inscripcion__usuario=request.user)
    return render(request, "pagos/historial_pagos.html", {"pagos": pagos})

def reembolso(request, pago_id):
    pago = get_object_or_404(Pago, pk=pago_id)
    if request.method == "POST":
        monto_raw = request.POST["monto"]
        error = None
        try:
            monto = Decimal(monto_raw)
            if monto <= 0 or monto > pago.monto:
                error = f"El monto debe ser positivo y no exceder el pago (${pago.monto})."
        except (InvalidOperation, ValueError):
            error = "Monto inválido. Escribe un número válido."
        if error:
            messages.error(request, error)
            return render(request, "pagos/reembolso_form.html", {"pago": pago})
        Reembolso.objects.create(
            pago=pago,
            monto=monto
        )
        return redirect("historial_pagos")
    return render(request, "pagos/reembolso_form.html", {"pago": pago})
