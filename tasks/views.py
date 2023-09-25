from django.shortcuts import render
from .models import Estudiante
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def iniciar_sesion(request):
    if request.method == 'POST':
        codigo_estudiante = request.POST['codigo_estudiante']
        password = request.POST['password']
        user = authenticate(request, codigo_estudiante=codigo_estudiante, password=password)
        print(user)
        print(codigo_estudiante)
        print(password)
        if user is not None:
            login(request, user)
            return redirect('inicio')  # Reemplaza 'inicio' con la URL de tu página principal
        else:
            # Autenticación fallida, muestra un mensaje de error
            return render(request, 'login.html', {'error_message': 'Código de estudiante o contraseña incorrectos.'})
    else:
        return render(request, 'login.html')
    
def inicio(request):
    return render(request,'home.html' )

def agregar_estudiante(request):
    if request.method == 'POST':
        # Obtiene los datos del formulario POST
        codigo_estudiante = request.POST.get('codigo_estudiante')
        password = request.POST.get('password')

        # Crea una instancia del modelo Estudiante con los datos del formulario
        nuevo_estudiante = Estudiante(codigo_estudiante=codigo_estudiante, password=password)

        # Guarda el estudiante en la base de datos
        nuevo_estudiante.save()

        # Redirige a una página de éxito o a donde desees
        return redirect('home.html')  # Reemplaza 'exito' con la URL correspondiente
    else:
        # Si la solicitud no es POST, muestra el formulario para agregar estudiantes
        return render(request, 'agregar.html')