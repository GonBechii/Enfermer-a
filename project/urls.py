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
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),

    #----- PRACTICANTE -------#
    path('panel/practicante/', views.panelPracticante, name='panel-practicante'),
    path('search/practicante/', views.searchPracticante, name='search-practicante'),
    path('panel/practicante/add/', views.panelPracticanteAdd, name='panel-practicante-add'),
    path('panel/practicante/<str:rut>/edit', views.panelPracticanteEdit, name='panel-practicante-edit'),
    #----- PACIENTE ----------#
    path('panel/paciente/', views.panelPaciente, name='panel-paciente'),
    path('search/paciente/', views.searchPaciente, name='search-paciente'),
    path('panel/paciente/add/', views.panelPacienteAdd, name='panel-paciente-add'),
    path('panel/paciente/<str:rut>/edit', views.panelPacienteEdit, name='panel-paciente-edit'),
    #----- ATENCIONES -------#
    path('panel/atencion/', views.panelAtencion, name='panel-atencion'),
    path('search/atencion/', views.searchAtencion, name='search-atencion'),
    path('panel/atencion/<str:rut>/add', views.panelAtencionAdd, name='panel-atencion-add'),
    path('panel/atencion/<int:id>/edit', views.panelAtencionEdit, name='panel-atencion-edit'),
    #----- Métricas -------#
    path('panel/metricas/practicantes/', views.metricasPracticantes, name='panel-metricas')
]
