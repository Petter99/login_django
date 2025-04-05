from django.shortcuts import render
from .models import User
from django.db import models
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .encriptacion import validatePassword, cryptPassword
from .forms import RegisterUserForm
from .forms import LoginUserForm
from django.http import HttpResponse
from django.contrib.auth import logout

def login_view(request):
    form = LoginUserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            try:
                user = User.objects.get(email=email)
                
                if validatePassword(password, user.password):
                    request.session['user_id'] = user.id
                    request.session['username'] = user.email
                    request.session.set_expiry(3600)
                #return dashboard
                    return redirect('dashboard')
                else:
                    return render(request, "error.html", {"error": "Contraseña incorrecta"})
            except User.DoesNotExist:
                return render(request, "error.html",{"error": "Usuario no encontrado"})
        else:
            return render(request, "login.html", {"form": form})
    else:
        #form = LoginUserForm()    
        return render(request, "login.html",{"form": form})

def register_view(request):
    form = RegisterUserForm(request.POST or None)
    if request.method == "POST":
        #form = RegisterUserForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            role = form.cleaned_data["role"]

            encrypted_password = cryptPassword(password)
            User.objects.create(email=email, password=encrypted_password, role=role)
            form = LoginUserForm()    
            return render(request, "login.html",{"form": form})
        else:
            return render(request, "register.html", {"form": form})
    else:
        #form = RegisterUserForm()
        return render(request, "register.html", {"form": form})

def dashboard_view(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        usuario = request.session['username']
        return HttpResponse(f'Bienvenido {usuario} Su ID es {user_id}')
    else: 
        return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')