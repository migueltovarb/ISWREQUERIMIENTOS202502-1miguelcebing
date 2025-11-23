from django.shortcuts import render
from .models import ReporteAsistencia, ReporteFinanciero

def asistencia_report(request):
    reportes = ReporteAsistencia.objects.all()
    return render(request, "reportes/asistencia.html", {"reportes": reportes})

def finanzas_report(request):
    reportes = ReporteFinanciero.objects.all()
    return render(request, "reportes/finanzas.html", {"reportes": reportes})
