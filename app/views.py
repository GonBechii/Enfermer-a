from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import Paciente, Practicante, Atencion
from .forms import PacienteForm, PracticanteForm, AtencionForm
import uuid 
import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.db.models import Count

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
        rut = request.POST.get('rut')
        atencion = Atencion.objects.filter(paciente__rut=rut)
        return render(request, 'pages/atencion/panel-atencion.html', {'rows': atencion})
    else:
        return render(request, 'pages/atencion/panel-atencion.html')
    
def panelAtencionAdd(request, rut):
    paciente = Paciente.objects.get(pk=rut)
    practicantes = Practicante.objects.all()
    if request.method == 'GET':
        return render(request, 'pages/atencion/panel-atencion-add.html', {
            'paciente': paciente,
            'practicantes': practicantes,
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

#--------- Métricas -----------#

def metricasPracticantes(request):
    if request.method == 'GET':
        # Obtener la cantidad de atenciones por motivo de consulta
        atenciones_por_motivo = (
            Atencion.objects
                .values('motivo_consulta')
                .annotate(cantidad=Count('id'))
        )

        #--Crea un gráfico de dona--#
        motivos = [item['motivo_consulta'] for item in atenciones_por_motivo]
        cantidad_atenciones = [item['cantidad'] for item in atenciones_por_motivo]

        # Calcular el total de atenciones
        total_atenciones = sum(cantidad_atenciones)

        fig, ax = plt.subplots(figsize=(8, 8))  # Ajustar el tamaño del gráfico

        wedges, texts, autotexts = ax.pie(
            cantidad_atenciones,
            autopct=lambda p: f'{int(p * total_atenciones / 100)} ({p:.1f}%)',
            textprops=dict(color="black"),  # Cambiar el color de los números a negro
            startangle=90,  # Ajustar el ángulo de inicio
            pctdistance=1.2  # Ajustar la distancia de los porcentajes desde el centro
        )

        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)

        # Añadir etiquetas con números y total de atenciones
        ax.text(0, 0, f'Total: {total_atenciones}\natenciones', ha='center', va='center', color='black', fontsize=12)

        ax.legend(wedges, motivos, title='Motivo de Consulta', loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

        plt.title('Porcentaje de Atenciones por Motivo de Consulta')

        plt.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1)

        # Guardar el gráfico de atenciones por motivo en un objeto BytesIO
        img_data_motivo = BytesIO()
        plt.savefig(img_data_motivo, format='png', bbox_inches='tight')
        img_data_motivo.seek(0)
        img_base64_motivo = base64.b64encode(img_data_motivo.read()).decode('utf-8')
        plt.close()

        # Obtener la cantidad de atenciones por practicante
        atenciones_por_practicante = (
            Atencion.objects
                .values('practicante__nombre')
                .annotate(cantidad=Count('id'))
        )

        #--Crea un gráfico de dona para cantidad de atenciones por practicante--#
        practicantes = [item['practicante__nombre'] for item in atenciones_por_practicante]
        cantidad_atenciones_practicante = [item['cantidad'] for item in atenciones_por_practicante]

        fig, ax = plt.subplots(figsize=(8, 8))  # Ajustar el tamaño del gráfico

        wedges, texts, autotexts = ax.pie(
            cantidad_atenciones_practicante,
            autopct=lambda p: f'{int(p * sum(cantidad_atenciones_practicante) / 100)} ({p:.1f}%)',
            textprops=dict(color="black"),
            startangle=90,
            pctdistance=1.2
        )

        # Añadir un círculo en el centro para crear un agujero (dona)
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)

        # Añadir etiquetas con números y total de atenciones
        ax.text(0, 0, f'Total: {sum(cantidad_atenciones_practicante)}\natenciones', ha='center', va='center',
                color='black', fontsize=12)

        ax.legend(wedges, practicantes, title='Practicantes', loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

        plt.title('Cantidad de Atenciones por Practicante')

        plt.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1)

        # Guardar el gráfico en un objeto BytesIO
        img_data_practicante = BytesIO()
        plt.savefig(img_data_practicante, format='png', bbox_inches='tight')
        img_data_practicante.seek(0)

        # Convertir la imagen en base64 para mostrarla en el template
        img_base64_practicante = base64.b64encode(img_data_practicante.read()).decode('utf-8')
        plt.close()

        return render(
            request,
            'pages/metricas/metricas-panel.html',
            {'img_base64_motivo': img_base64_motivo, 'img_base64_practicante': img_base64_practicante}
        )


