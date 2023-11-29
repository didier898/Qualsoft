from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .models import Proyecto

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

def mis_proyectos(request):
    # Obtén todos los proyectos del usuario actual
    proyectos = Proyecto.objects.filter(usuario=request.user)

    # Puedes agregar más contexto según sea necesario

    return render(request, 'core/mis_proyectos.html', {'proyectos': proyectos})

class CrearProyectoView(View):
    template_name = 'core/crear_proyecto.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class EstablecerRequisitosView(View):
    template_name = 'core/establecer_requisitos.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class EspecificarEvaluacionView(View):
    template_name = 'core/especificar_evaluacion.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class EvaluarProductoView(View):
    template_name = 'core/evaluar_producto.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class IngresarObjetivoDescripcionView(View):
    template_name = 'core/ingresar_objetivo_descripcion.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    
class IdentificarProductoView(View):
    template_name = 'core/identificar_producto.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    
class IdentificarRequerimientosView(View):
    template_name = 'core/identificar_requerimientos.html'

    def get(self, request, *args, **kwargs):
        # Aquí podrías recuperar los requerimientos de calidad de la base de datos si ya se han agregado
        requerimientos = [
            {'categoria': 'Funcionalidad', 'descripcion': 'El software debe cumplir con los requisitos funcionales especificados en la documentación.'},
            # ... Otros requerimientos
        ]
        return render(request, self.template_name, {'requerimientos': requerimientos})