from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    class Meta:
        permissions = [
            ("view_agregar_tarea", "Puede ver la sección de agregar tarea"),
            ("view_lista_tareas", "Puede ver la sección de lista de tareas"),
            ("view_detalle_tarea", "Puede ver la sección de detalle de tarea"),
        ]    