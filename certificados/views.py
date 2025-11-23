from django.shortcuts import render, get_object_or_404
from .models import Certificado

def descargar(request, certificado_id):
    certificado = Certificado.objects.filter(id=certificado_id).first()
    if not certificado:
        return render(request, "certificados/descargar.html", {"certificado": None, "error": "No existe el certificado solicitado."})
    return render(request, "certificados/descargar.html", {"certificado": certificado})

def verificar(request):
    codigo = request.GET.get("codigo")
    certificado = Certificado.objects.filter(codigo_verificacion=codigo).first()
    valido = certificado is not None
    return render(request, "certificados/verificar.html", {"valido": valido, "certificado": certificado})
