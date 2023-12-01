from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .models import Proyecto
from .forms import ObjetivoForm
from django.shortcuts import render, redirect
from django.views import View
from .models import Proyecto, Producto
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Proyecto
from django.shortcuts import render, redirect
from django.views import View
from .models import Producto
from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Proyecto, Producto
from django.shortcuts import render, redirect
from django.views import View
from .models import Producto
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from .forms import ObjetivoForm
from .models import Producto
from django.shortcuts import render, redirect
from django.views import View
from .models import Proyecto, Producto
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CrearProyectoForm
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from .forms import ObjetivoForm
from .models import Producto
# En tu archivo views.py
from django.shortcuts import render, redirect
from django.views import View
from .forms import IdentificarProductoForm
from .models import Producto
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Requisito
from .forms import RequisitoForm
from django.shortcuts import get_object_or_404

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

@login_required
def mis_proyectos(request):
    # Obtén todos los proyectos del usuario actual
    proyectos = Proyecto.objects.filter(usuario=request.user)

    return render(request, 'core/mis_proyectos.html', {'proyectos': proyectos})

@method_decorator(login_required, name='dispatch')
class CrearProyectoView(View):
    template_name = 'core/crear_proyecto.html'

    def get(self, request, *args, **kwargs):
        form = CrearProyectoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CrearProyectoForm(request.POST)

        if form.is_valid():
            nombre_proyecto = form.cleaned_data['nombre_proyecto']
            fecha_proyecto = form.cleaned_data['fecha_proyecto']
            nombre_producto = form.cleaned_data['nombre_producto']

            # Crear un nuevo proyecto
            proyecto = Proyecto.objects.create(
                nombre_proyecto=nombre_proyecto,
                fecha_proyecto=fecha_proyecto,
                usuario=request.user,
            )

            # Crear un nuevo producto asociado al proyecto
            producto = Producto.objects.create(
                id_proyecto=proyecto,
                nombre_producto=nombre_producto,
                tipo_producto='',  # Agrega un valor para el tipo_producto
                usuario=request.user,  # Asigna el usuario actual al campo usuario
            )

            # Asignar el producto al proyecto
            proyecto.producto = producto
            proyecto.save()

            # Redireccionar a la siguiente etapa del proceso
            return redirect('establecer_requisitos')
        else:
            # Manejar el caso en que el formulario no sea válido
            print("El formulario no es válido.")

        return render(request, self.template_name, {'form': form})



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
        form = ObjetivoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ObjetivoForm(request.POST)

        if form.is_valid():
            objetivos_descripcion = form.cleaned_data['objetivos_descripcion']

            # Obtén el producto actual del usuario
            producto = request.user.productos.first()

            if producto:
                # Actualiza el campo 'objetivo_producto' del producto con la descripción ingresada
                producto.objetivo_producto = objetivos_descripcion
                producto.save()
                print(f'Objetivo Producto después de guardar: {producto.objetivo_producto}')

                # Redirige a otra vista o muestra un mensaje de éxito, según tu lógica
                return redirect('crear_proyecto')
            else:
                # Manejar el caso en que no se encuentre un producto
                print('No se encontró un producto asociado al usuario.')

        return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class IdentificarProductoView(View):
    template_name = 'core/identificar_producto.html'

    def get(self, request, *args, **kwargs):
        form = IdentificarProductoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = IdentificarProductoForm(request.POST)

        if form.is_valid():
            tipo_producto = form.cleaned_data['tipo_producto']

            # Obtén el producto actual del usuario
            producto = request.user.productos.first()

            if producto:
                # Actualiza el campo 'tipo_producto' del producto con la elección realizada
                producto.tipo_producto = tipo_producto
                producto.save()

                # Redirige a otra vista o muestra un mensaje de éxito, según tu lógica
                return redirect('crear_proyecto')  # Reemplaza 'otra_vista' con el nombre de la vista a la que deseas redirigir
            else:
                # Manejar el caso en que no se encuentre un producto
                print('No se encontró un producto asociado al usuario.')

        return render(request, self.template_name, {'form': form})
       
    
class IdentificarRequerimientosView(View):
    template_name = 'core/identificar_requerimientos.html'

    def get(self, request, *args, **kwargs):
        form = RequisitoForm()
        requisitos = Requisito.objects.all()
        return render(request, self.template_name, {'form': form, 'requisitos': requisitos})

    def post(self, request, *args, **kwargs):
        form = RequisitoForm(request.POST)

        if form.is_valid():
            descripcion = form.cleaned_data['descripcion']

            # Crear un nuevo requisito
            requisito = Requisito.objects.create(descripcion=descripcion)

            # Redireccionar a la misma vista para mostrar el nuevo requisito
            return redirect('identificar_requerimientos')
        else:
            # Manejar el caso en que el formulario no sea válido
            print("El formulario no es válido.")

        requisitos = Requisito.objects.all()
        return render(request, self.template_name, {'form': form, 'requisitos': requisitos})
    
    
    

class EliminarRequerimientoView(View):
    template_name = 'core/eliminar_requerimiento.html'  # Puedes crear esta plantilla si es necesario

    def get(self, request, requisito_id, *args, **kwargs):
        requisito = get_object_or_404(Requisito, pk=requisito_id)
        requisito.delete()
        return redirect('identificar_requerimientos')
