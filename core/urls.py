# En core/urls.py

from django.urls import path
from . import views
from .views import inicio_sesion, registro, principal, mis_proyectos
from .views import CrearProyectoView, EstablecerRequisitosView, EspecificarEvaluacionView, EvaluarProductoView
#ConcluirEvaluacionView
from .views import EstablecerRequisitosView
from .views import IngresarObjetivoDescripcionView
from .views import EspecificarEvaluacionView
from .views import IdentificarRequerimientosView
#RiesgosEvaluacionView, CaracteristicasEvaluacionView, SubcaracteristicasEvaluacionView, AtributosEvaluacionView, CriteriosAprobacionView
#from .views import EjecutarPruebaView, ObtenerResultadosView
#from .views import ConcluirEvaluacionView, GenerarInformeDetalladoView, GenerarInformeGeneralView, GenerarInformeRecomendacionesView
from .views import IdentificarProductoView

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Ruta para la vista de inicio
    path('inicio-sesion/', inicio_sesion, name='inicio_sesion'),
    path('registro/', registro, name='registro'),
    path('principal/', principal, name='principal'),
    path('mis_proyectos/', mis_proyectos, name='mis_proyectos'),
    path('crear_proyecto/', CrearProyectoView.as_view(), name='crear_proyecto'),
    path('establecer_requisitos/', EstablecerRequisitosView.as_view(), name='establecer_requisitos'),
    path('ingresar_objetivo_descripcion/', IngresarObjetivoDescripcionView.as_view(), name='ingresar_objetivo_descripcion'),
    path('identificar_producto/', IdentificarProductoView.as_view(), name='identificar_producto'),
    path('especificar_evaluacion/', EspecificarEvaluacionView.as_view(), name='especificar_evaluacion'),
    path('identificar_requerimientos/', IdentificarRequerimientosView.as_view(), name='identificar_requerimientos'),
    path('evaluar_producto/', EvaluarProductoView.as_view(), name='evaluar_producto'),
    #path('concluir_evaluacion/', ConcluirEvaluacionView.as_view(), name='concluir_evaluacion'),
    #path('riesgos_evaluacion/', RiesgosEvaluacionView.as_view(), name='riesgos_evaluacion'),
    #path('caracteristicas_evaluacion/', CaracteristicasEvaluacionView.as_view(), name='caracteristicas_evaluacion'),
    #path('subcaracteristicas_evaluacion/', SubcaracteristicasEvaluacionView.as_view(), name='subcaracteristicas_evaluacion'),
    #path('atributos_evaluacion/', AtributosEvaluacionView.as_view(), name='atributos_evaluacion'),
    #path('criterios_aprobacion/', CriteriosAprobacionView.as_view(), name='criterios_aprobacion'),
    #path('ejecutar_prueba/', EjecutarPruebaView.as_view(), name='ejecutar_prueba'),
    #path('obtener_resultados/', ObtenerResultadosView.as_view(), name='obtener_resultados'),
    #path('concluir_evaluacion/', ConcluirEvaluacionView.as_view(), name='concluir_evaluacion'),
    #path('generar_informe_detallado/', GenerarInformeDetalladoView.as_view(), name='generar_informe_detallado'),
    #path('generar_informe_general/', GenerarInformeGeneralView.as_view(), name='generar_informe_general'),
    #path('generar_informe_recomendaciones/', GenerarInformeRecomendacionesView.as_view(), name='generar_informe_recomendaciones'),
]