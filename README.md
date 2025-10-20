# Evaluacion_Modulo_6

📝 Gestor de Tareas 
    desarrollado por Sofía Lagos
    Bootcamp Desarrollo Full Stack Python

Este es un proyecto simple de gestión de tareas desarrollado con Django y Bootstrap 5, creado durante el Bootcamp de Desarrollo Full Stack Python. Permite a los usuarios registrarse, iniciar sesión, y gestionar una lista de tareas pendientes.
El objetivo principal fue aplicar los conocimientos de autenticación de Django y el manejo de flujos CRUD (Crear, Leer, Actualizar, Eliminar) dentro de una aplicación web.

✨ Funcionalidades Principales

Implementé las siguientes características clave:

    Autenticación de Usuario: Permite a los usuarios Registrarse y Iniciar/Cerrar Sesión con un modelo de usuario personalizado (CustomUser).

    Gestión de Tareas (CRUD Básico):

        Ver Tareas: Lista todas las tareas creadas por el usuario autenticado.

        Agregar Tarea: Permite añadir tareas con Título, Descripción y Fecha de Vencimiento.

        Ver Detalle: Muestra la información completa de una tarea.

        Eliminar Tarea: Permite borrar tareas después de una confirmación.

        Marcar Estado: Permite cambiar el estado de la tarea entre "Pendiente" y "Completada".

    Seguridad: Todas las vistas de gestión de tareas están protegidas con @login_required para asegurar que solo usuarios autenticados puedan acceder a ellas.

    Mensajes de Usuario: Uso de django.contrib.messages para dar feedback (éxito, error, etc.) después de acciones como agregar o eliminar una tarea.

⚙️ Estructura del Proyecto

El proyecto está centrado en la aplicación tareas/:

    tareas/views.py: Contiene la lógica de las funciones, incluyendo la manipulación de las tareas almacenadas en la lista tareas_en_memoria (Importante! Las tareas se pierden al reiniciar el servidor, ya que solo están en RAM :D).

    tareas/urls.py: Define todas las rutas de la aplicación, como /tareas/, /agregar_tarea/, /login/, etc.

    templates/:

        base.html: El layout principal con navbar, footer y manejo de mensajes flash.

        lista_tareas.html: La vista principal de las tareas.

        agregar_tareas.html: Muestra un formulario sencillo con campos para el título, la descripción y la fecha de vencimiento de una nueva tarea. Utiliza el método POST para enviar los datos a la vista correspondiente.

        detalle_tarea.html: Muestra la información completa de una tarea específica, incluyendo su título, descripción, fecha de vencimiento y estado, todo en formato de tarjeta.

        eliminar_tarea.html: Muestra una página de confirmación simple. Pregunta al usuario si está seguro de eliminar la tarea seleccionada antes de ejecutar la acción.

        index.html: La página de bienvenida del sitio. Muestra un mensaje introductorio y contiene botones grandes para redirigir al usuario a "Iniciar sesión" y "Registrarse".

        login.html: Contiene un formulario para iniciar sesión (campos de Usuario y Contraseña). Si el usuario intenta acceder a una vista protegida, es redirigido aquí.

        register.html: Contiene el formulario de registro de usuario (Usuario, Correo electrónico, Contraseña y Confirmar Contraseña), utilizando el formulario personalizado Form_Registro.


    settings.py: Configuración básica, incluyendo la definición de mi AUTH_USER_MODEL = 'tareas.CustomUser'.

🚀 Cómo Ejecutar el Proyecto

1. Clonar el Repositorio

```bash
git clone <https://github.com/too0oori/Evaluacion_Modulo_6>
cd gestor_tareas
```

2. Configurar el Entorno Virtual

Aislar las dependencias del proyecto.

Crear el entorno virtual (env es un nombre común)
python -m venv env

Activar el entorno virtual
En Windows (Command Prompt):
```bash
env\Scripts\activate
```
3. Instalar Dependencias

```bash
pip install -r requirements.txt
```
Pero como se utiliza Python se puede instalar directamente en el entorno virtual con

```bash
pip install django
```

4. Ejecutar Migraciones

El proyecto usa un modelo CustomUser, por lo que necesitarás aplicar las migraciones a la base de datos SQLite predeterminada.

```bash
python manage.py makemigrations tareas
python manage.py migrate
```

6. Iniciar el Servidor

Ejecuta el servidor de desarrollo de Django:

```bash

python manage.py runserver
```


Proyecto desarrollado por **Sofía Lagos**  
📚 Bootcamp Desarrollo Full Stack Python — Módulo 3  
🌐 GitHub: [github.com/too0oori](https://github.com/too0oori)

