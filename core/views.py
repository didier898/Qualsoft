from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def inicio(request):
    return render(request, 'core/inicio.html')

def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('principal')  # Cambia 'pagina_inicio' a la URL deseada después del inicio de sesión
        else:
            # Manejar error de inicio de sesión fallido, puedes agregar un mensaje de error si lo deseas
            pass

    return render(request, 'core/inicio_sesion.html')


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Puedes personalizar esto según tus necesidades, por ejemplo, redirigir a la página de inicio de sesión
            return redirect('inicio_sesion')
    else:
        form = UserCreationForm()

    return render(request, 'core/registro.html', {'form': form})

def principal(request):
    # Puedes agregar lógica adicional aquí si es necesario
    return render(request, 'core/principal.html')