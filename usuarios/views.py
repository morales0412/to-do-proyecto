from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import RegistroForm, LoginForm


def registro_view(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    usuario = form.save(commit=False)
                    usuario.save()
                    print(f"✓ Usuario guardado: {usuario.username} (ID: {usuario.id})")
                login(request, usuario)
                return redirect("to_do_app:task_list")
            except Exception as e:
                print(f"✗ Error guardando usuario: {e}")
                form.add_error(None, f"Error al guardar: {e}")
        else:
            print(f"Errores del formulario: {form.errors}")
    else:
        form = RegistroForm()

    return render(request, "registro.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect("to_do_app:task_list")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


@login_required(login_url="usuarios:login")
def logout_view(request):
    logout(request)
    return redirect("usuarios:login")
