# ecosistema

# Proyecto Django

Este es un proyecto web construido con el framework Django.

## Requisitos

- Python 3.8+
- Django 3.2+
- pip (Python package installer)
- virtualenv (opcional, pero recomendado)

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/tu_proyecto.git
    cd tu_proyecto
    ```

2. Crea un entorno virtual (opcional, pero recomendado):

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Configura las variables de entorno:

    Crea un archivo [.env](http://_vscodecontentref_/1) en el directorio raíz del proyecto y añade las siguientes variables:

    ```env
    SECRET_KEY=tu_secreto
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DATABASE_URL=sqlite:///db.sqlite3
    ```

5. Realiza las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

6. Crea un superusuario para acceder al panel de administración:

    ```bash
    python manage.py createsuperuser
    ```

7. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

8. Abre tu navegador y visita `http://127.0.0.1:8000` para ver la aplicación en funcionamiento.

## Estructura del Proyecto

```plaintext
tu_proyecto/
├── manage.py
├── tu_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── tu_proyecto/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
├── templates/
└── requirements.txt
