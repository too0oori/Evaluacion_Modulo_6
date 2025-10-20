from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import Form, CharField, Textarea
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from .forms import Form_Registro
from django.http import Http404
from django.forms import Form, CharField, Textarea, DateField, ChoiceField


class TareaForm(Form):
    titulo = CharField(max_length=100, label='Título')
    descripcion = CharField(widget=forms.Textarea, label='Descripción')
    fecha_vencimiento = DateField(label='Fecha de Vencimiento' , widget=forms.DateInput(attrs={'type': 'date'}))

#las tareas se almacenan temporalmente en memoria y se perderán al reiniciar el servidor
tareas_en_memoria = []
id_counter = 1

def index(request):
    return render(request, 'index.html')

@login_required
def lista_tareas(request):
    tareas_usuario = [tarea for tarea in tareas_en_memoria if tarea['usuario'] == request.user.username]
    return render(request, 'lista_tareas.html', {'tareas': tareas_usuario})

@login_required
def detalle_tarea(request, tarea_id):
    tarea = get_object_or_404_from_list( #es una función auxiliar para simular el comportamiento de get_object_or_404 para listas
        [tarea for tarea in tareas_en_memoria if tarea['usuario'] == request.user.username],
        id=tarea_id
    )
    return render(request, 'detalle_tarea.html', {'tarea': tarea})

@login_required
def agregar_tarea(request):
    global id_counter # necesario para modificar el contador global de IDs
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            # Se crea el diccionario con los datos de la tarea
            tarea = {
                'id': id_counter,
                'titulo': form.cleaned_data['titulo'],
                'descripcion': form.cleaned_data['descripcion'],
                'fecha_vencimiento': form.cleaned_data['fecha_vencimiento'],
                'estado': 'pendiente',
                'usuario': request.user.username
            }
            id_counter += 1 # aumentar el contador global
            tareas_en_memoria.append(tarea)
            messages.success(request, 'Tarea agregada exitosamente.')
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'agregar_tarea.html', {'form': form})

@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404_from_list(
        [tarea for tarea in tareas_en_memoria if tarea['usuario'] == request.user.username],
        id=tarea_id
    )
    if request.method == 'POST':
        tareas_en_memoria.remove(tarea)
        messages.success(request, 'Tarea eliminada exitosamente.')
        return redirect('lista_tareas')
    return render(request, 'eliminar_tarea.html', {'tarea': tarea})

#Funcion para marcar como completada una tarea
@login_required
def marcar_completada(request, tarea_id):
    tarea = next((t for t in tareas_en_memoria if t['usuario'] == request.user.username and t['id'] == tarea_id), None) #para buscar en la lista correspondiente solo a un usuario definido y no de otros usuarios
    
    if tarea is None:
        messages.error(request, 'Tarea no encontrada.')
        return redirect('lista_tareas')
    
    # Cambiar el estado
    if tarea['estado'] == 'pendiente':
        tarea['estado'] = 'completada'
        messages.success(request, f'Tarea "{tarea["titulo"]}" marcada como completada.')
    else:
        tarea['estado'] = 'pendiente'
        messages.info(request, f'Tarea "{tarea["titulo"]}" marcada como pendiente.')
    
    return redirect('lista_tareas')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('lista_tareas')
    # Implementa la lógica de inicio de sesión aquí
    if request.method == 'POST':
        # Autenticar y redirigir
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Autenticación de usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_tareas')
        else:
            messages.error(request, 'Credenciales inválidas.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente.')
    return redirect('login')

# Formulario de registro
def register_view(request):
    if request.method == 'POST':
        form = Form_Registro(request.POST) #se usa un formulario personalizado basado en UserCreationForm.
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = Form_Registro()
    return render(request, 'register.html', {'form': form})

# Función auxiliar cuando no encuentra el objeto en la lista, da error 404
def get_object_or_404_from_list(list_, **kwargs):
    for item in list_:
        match = True
        for key, value in kwargs.items():
            if item.get(key) != value:
                match = False
                break
        if match:
            return item
    raise Http404("No se encontró el objeto.")