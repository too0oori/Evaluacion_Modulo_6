from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tarea
from django.forms import Form, CharField, Textarea
from django.contrib import messages


class TareaForm(Form):
    titulo = CharField(max_length=100, label='Título')
    descripcion = CharField(widget=forms.Textarea, label='Descripción')

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
    tarea = get_object_or_404(Tarea, id=tarea_id, usuario=request.user)
    return render(request, 'detalle_tarea.html', {'tarea': tarea})

@login_required
def agregar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = Tarea(
                titulo=form.cleaned_data['titulo'],
                descripcion=form.cleaned_data['descripcion'],
                usuario=request.user
            )
            tareas_en_memoria.append(tarea)
            messages.success(request, 'Tarea agregada exitosamente.')
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'agregar_tarea.html', {'form': form})

@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, usuario=request.user)
    if request.method == 'POST':
        tarea.delete()
        messages.success(request, 'Tarea eliminada exitosamente.')
        return redirect('lista_tareas')
    return render(request, 'eliminar_tarea.html', {'tarea': tarea})