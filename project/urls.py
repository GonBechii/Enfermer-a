"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    #----- PRACTICANTE -------#
    path('panel/practicante/', views.panelPracticante, name='panel-practicante'),
    path('search/practicante/', views.searchPracticante, name='search-practicante'),
    path('panel/practicante/add/', views.panelPracticanteAdd, name='panel-practicante-add'),
    path('panel/practicante/<int:rut>/edit', views.panelPracticanteEdit, name='panel-practicante-edit'),
    path('panel/practicante/<str:rut>', views.panelPracticanteBloq, name='panel-practicante-bloq'),
    #----- PACIENTE ----------#
    path('panel/paciente/', views.panelPaciente, name='panel-paciente'),
    path('search/paciente/', views.searchPaciente, name='search-paciente'),
    path('panel/paciente/add/', views.panelPacienteAdd, name='panel-paciente-add'),
    path('panel/paciente/<int:rut>/edit', views.panelPacienteEdit, name='panel-paciente-edit'),
    path('panel/paciente/<str:rut>', views.panelPacienteBloq, name='panel-paciente-bloq'),
    #----- ATENCIONES -------#
    path('panel/atencion/', views.panelAtencion, name='panel-atencion'),
    path('search/atencion/', views.searchAtencion, name='search-atencion'),
    path('panel/atencion/<int:rut>/add', views.panelAtencionAdd, name='panel-atencion-add'),
    path('panel/atencion/<int:id>/edit', views.panelAtencionEdit, name='panel-atencion-edit'),
    path('panel/atencion/<int:id>/delete', views.panelAtencionDelete, name='panel-atencion-delete'),
    #----- METRICAS -------#
    path('panel/metricas/', views.panelMetricas, name='panel-metricas'),
]
