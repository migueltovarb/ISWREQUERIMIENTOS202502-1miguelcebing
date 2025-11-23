from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Usuario
from django.contrib import messages
from django.contrib.auth.hashers import make_password

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Credenciales inválidas")
    return render(request, "usuarios/login.html")

def registro_view(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        rol = request.POST.get("rol")  # <-- CORREGIDO, toma el rol del form
        if Usuario.objects.filter(username=username).exists():
            messages.error(request, "Ese usuario ya existe")
        elif Usuario.objects.filter(email=email).exists():
            messages.error(request, "Ese correo ya está registrado")
        else:
            user = Usuario.objects.create_user(
                username=username,
                email=email,
                password=password,
                nombre=nombre,
                rol=rol  # <-- usa el rol proporcionado
            )
            login(request, user)
            return redirect("home")
    return render(request, "usuarios/registro.html")

@login_required
def lista_usuarios(request):
    if request.user.rol != "administrador":
        return HttpResponseForbidden("Acceso solo para administradores.")
    usuarios = Usuario.objects.all()
    return render(request, "usuarios/lista_usuarios.html", {"usuarios": usuarios})

@login_required
def crear_usuario(request):
    if request.user.rol != "administrador":
        return HttpResponseForbidden("Acceso solo para administradores.")
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        rol = request.POST.get("rol")
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "Este correo ya está registrado.")
            return render(request, "usuarios/crear_usuario.html")
        if Usuario.objects.filter(username=username).exists():
            messages.error(request, "Este usuario ya está registrado.")
            return render(request, "usuarios/crear_usuario.html")
        user = Usuario.objects.create_user(
            username=username, email=email, password=password,
            nombre=nombre, rol=rol
        )
        return redirect("lista_usuarios")
    return render(request, "usuarios/crear_usuario.html")

@login_required
def editar_usuario(request, pk):
    if request.user.rol != "administrador":
        return HttpResponseForbidden("Acceso solo para administradores.")
    user = Usuario.objects.get(pk=pk)
    if request.method == "POST":
        user.nombre = request.POST.get("nombre")
        user.email = request.POST.get("email")
        user.rol = request.POST.get("rol")
        user.save()
        return redirect("detalle_usuario", pk=user.pk)
    return render(request, "usuarios/editar_usuario.html", {"usuario": user})

@login_required
def eliminar_usuario(request, pk):
    if request.user.rol != "administrador":
        return HttpResponseForbidden("Acceso solo para administradores.")
    user = Usuario.objects.get(pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect("lista_usuarios")
    return render(request, "usuarios/eliminar_usuario.html", {"usuario": user})

@login_required
def detalle_usuario(request, pk):
    if request.user.rol != "administrador":
        return HttpResponseForbidden("Acceso solo para administradores.")
    user = Usuario.objects.get(pk=pk)
    return render(request, "usuarios/detalle_usuario.html", {"usuario": user})

@login_required
def perfil(request):
    return render(request, "usuarios/perfil.html", {"usuario": request.user})

@login_required
def cambiar_contrasena(request, pk):
    if request.user.rol != "administrador":
        return HttpResponseForbidden("Acceso solo para administradores.")
    usuario = Usuario.objects.get(pk=pk)
    if request.method == "POST":
        nueva_contrasena = request.POST.get("password")
        if nueva_contrasena:
            usuario.password = make_password(nueva_contrasena)
            usuario.save()
            messages.success(request, "Contraseña actualizada correctamente.")
            return redirect("lista_usuarios")
        else:
            messages.error(request, "Debes ingresar una nueva contraseña.")
    return render(request, "usuarios/cambiar_contrasena.html", {"usuario": usuario})