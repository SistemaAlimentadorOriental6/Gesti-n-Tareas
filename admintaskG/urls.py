"""
URL configuration for admintaskG project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from admintaskG.views import login, listadoComites, logout_view, agregarComite, agregarTarea, listadoTareas, listadoSubtareas, agregarSubtarea, listadoSubtareasAdicionales, agregarSubtareaAdicional, estadoTarea, estadoSubtarea, estadoSubtareaAdicional, tareas_por_comite, subtareas_por_tarea, subtareasadicionales_por_subtarea, enviar_pdf_individualizado, obtener_estado_envio, filtrar_por_responsable

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('Comites/listadoComites', listadoComites, name='listadoComites'),
    path('Comites/agregarComite', agregarComite, name='agregarComite'),
    path('Tareas/agregarTarea', agregarTarea, name='agregarTarea'),
    path('Tareas/listadoTareas/<int:comite_id>/', listadoTareas, name='listadoTareas'),
    path('Subtareas/listadoSubtareas/<int:tarea_id>/', listadoSubtareas, name='listadoSubtareas'),
    path('Subtareas/agregarSubtarea', agregarSubtarea, name='agregarSubtarea'),
    path('SubtareasAdicionales/listadoSubtareasAdicionales/<int:subtarea_id>/',listadoSubtareasAdicionales , name='listadoSubtareasAdicionales'),
    path('SubtareasAdicionales/agregarSubtareaAdicional', agregarSubtareaAdicional , name='agregarSubtareaAdicional'),
    
    path('Tareas/estadoTarea/<int:tarea_id>', estadoTarea, name='estadoTarea'),
    path('Subtareas/estadoSubtarea/<int:subtarea_id>', estadoSubtarea, name='estadoSubtarea'),
    path('SubtareasAdicionales/estadoSubtareaAdicional/<int:subtareaadicional_id>', estadoSubtareaAdicional, name='estadoSubtareaAdicional'),
    

    path('ajax/tareas/<int:comite_id>/', tareas_por_comite, name='ajax_tareas'),
    path('ajax/subtareas/<int:tarea_id>/', subtareas_por_tarea, name='ajax_subtareas'), 
    path('ajax/subtareasadicionales/<int:subtarea_id>/', subtareasadicionales_por_subtarea, name='ajax_subtareasadicionales'),
    
    path('pdf/<int:comite_id>/enviar-pdf/', enviar_pdf_individualizado, name='enviar_pdf_individualizado'),
    path('tareas/estado-envio/', obtener_estado_envio, name='obtener_estado_envio'),
    



    path('ajax/filtrar/<int:comite_id>/', filtrar_por_responsable, name='filtrar_por_responsable'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
