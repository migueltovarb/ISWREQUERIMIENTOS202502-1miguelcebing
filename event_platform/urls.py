from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.contrib.auth.views import LogoutView

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', home, name='home'),  # Página principal
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('eventos/', include('eventos.urls')),
    path('inscripciones/', include('inscripciones.urls')),
    path('pagos/', include('pagos.urls')),
    path('certificados/', include('certificados.urls')),
    path('reportes/', include('reportes.urls')),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # ← Esta línea habilita {% url 'logout' %}
]
