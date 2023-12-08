from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import Paciente, Practicante, Atencion
from .forms import PacienteForm, PracticanteForm, AtencionForm
import uuid 
import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

    if user is None:
        return render(request, 'signin.html', {
            'error': 'User or password is incorrect'
        })
    else:
        login(request, user)
        return redirect('panel-practicante')
    
#--------- PRACTICANTE -----------# 

def panelPracticante(request):
    if request.method == 'GET':
        rows = Practicante.objects.all()
        return render(request, 'pages/practicante/panel-practicante.html',{
            'rows': rows
        })

def searchPracticante(request):
    if request.method == 'POST':
        practicante = Practicante.objects.get(pk=request.POST['rut'])

        return render(request, 'pages/practicante/panel-practicante.html',{
            'rows': [practicante]
        })
    else:
        return render(request, 'pages/practicante/panel-practicante.html')

def panelPracticanteAdd(request):
    if request.method == 'GET':
        return render(request, 'pages/practicante/panel-practicante-add.html')
    else:
        form = PracticanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('panel-practicante')
        else:
            # Render de error
            return render(request, 'pages/practicante/panel-practicante-add.html', {'form': form})
    
def panelPracticanteEdit(request, rut):
    user = Practicante.objects.get(pk=rut)
    if request.method == 'GET':
        return render(request, 'pages/practicante/panel-practicante-edit.html',{
            "user": user
        })
    else:
        form = PracticanteForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('panel-practicante')
        return render(request, 'pages/practicante/panel-practicante-edit.html',
        {
            "user": user
        })
     
#--------- PACIENTE -----------# 
def panelPaciente(request):
    if request.method == 'GET':
        rows = Paciente.objects.all()
        return render(request, 'pages/paciente/panel-paciente.html',{
            'rows': rows
        })
    else:
        return render(request, 'pages/paciente/panel-paciente.html')
    
def searchPaciente(request):
    if request.method == 'POST':
        paciente = Paciente.objects.get(pk=request.POST['rut'])

        return render(request, 'pages/paciente/panel-paciente.html',{
            'rows': [paciente]
        })
    else:
        return render(request, 'pages/paciente/panel-paciente.html')
    
def panelPacienteAdd(request):
    if request.method == 'GET':
        return render(request, 'pages/paciente/panel-paciente-add.html')
    else:
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('panel-paciente')
        else:
            print("ERROR: ", form.errors)
            return render(request, 'pages/paciente/panel-paciente-add.html', {
                'error': 'El formulario es invalido'
            })

def panelPacienteEdit(request, rut):
    user = Paciente.objects.get(pk=rut)
    if request.method == 'GET':
        return render(request, 'pages/paciente/panel-paciente-edit.html',{
            "user": user
        })
    else:
        form = PacienteForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('panel-paciente')
        return render(request, 'pages/paciente/panel-paciente-edit.html',{
            "user": user
        })

#--------- ATENCION -----------# 
def panelAtencion(request):
    if request.method == 'GET':
        rows = Atencion.objects.all()
        return render(request, 'pages/atencion/panel-atencion.html',{
            'rows': rows
        })
    else:
        return render(request, 'pages/atencion/panel-atencion.html')
    
def searchAtencion(request):
    if request.method == 'POST':
        atencion = Atencion.objects.get(pk=request.POST['id'])

        return render(request, 'pages/atencion/panel-atencion.html',{
            'rows': [atencion]
        })
    else:
        return render(request, 'pages/atencion/panel-atencion.html')
    
def panelAtencionAdd(request, rut):
    paciente = Paciente.objects.get(pk=rut)
    if request.method == 'GET':
        return render(request, 'pages/atencion/panel-atencion-add.html', {
            'paciente': paciente,
            'error': 'El formulario es invalido'
        })

    else:
        form = AtencionForm(request.POST)
        if form.is_valid():
            atencion = form.save(commit=False)
            atencion.id = len(Atencion.objects.all()) + 1
            atencion.paciente =  paciente
            atencion.fechaInicio = datetime.datetime.now()
            atencion.fechaTermino = datetime.datetime.now()
            atencion.save()
            return redirect('panel-atencion')
        print(form.errors)
        return render(request, 'pages/atencion/panel-atencion-add.html', {
            'paciente': [paciente],
            'error': 'El formulario es invalido'
        })

def panelAtencionEdit(request, id):
    atencion = Atencion.objects.get(pk=id)
    if request.method == 'GET':
        return render(request, 'pages/atencion/panel-atencion-edit.html',{
            "atencion": atencion
        })
    else:
        form = AtencionForm(request.POST, instance=atencion)
        if form.is_valid():
            form.save()
            return redirect('panel-atencion')
        return render(request, 'pages/atencion/panel-atencion-edit.html',{
            "atencion": atencion
        })



