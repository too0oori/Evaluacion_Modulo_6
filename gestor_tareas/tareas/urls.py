from django import forms
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tareas/', views.lista_tareas, name='lista_tareas'),
    path('agregar_tarea/', views.agregar_tarea, name='agregar_tarea'),
    path('eliminar_tarea/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('detalle_tarea/<int:tarea_id>/', views.detalle_tarea, name='detalle_tarea'),
    path('marcar_completada/<int:tarea_id>/', views.marcar_completada, name='marcar_completada'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]