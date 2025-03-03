Guía para Ejecutar el Proyecto
* Configurar el Entorno Virtual
Antes de correr el proyecto, se recomienda crear un entorno virtual para aislar las dependencias.

--En Windows (CMD o PowerShell):
>> python -m venv venv
>> venv\Scripts\activate

--En macOS / Linux:

>> python3 -m venv venv
>> source venv/bin/activate

--Acceder al Proyecto
Dirígete a la carpeta del backend:
>> cd 20250302_PruebaTecnica/backend

--Instalar Dependencias y Ejecutar el Proyecto
Ejecuta los siguientes comandos para configurar la base de datos y correr el servidor:

>> pip install -r requirements.txt  # Instalar dependencias
>> python manage.py makemigrations   # Generar migraciones
>> python manage.py migrate          # Aplicar migraciones
>> python manage.py runserver        # Iniciar servidor local
El proyecto estará disponible en: http://127.0.0.1:8000/

--Probar la API con Postman o Thunder Client
Endpoint:    POST http://127.0.0.1:8000/api/app_matching/find-best-match/
Request (JSON):
{
    "elements": [
        {"nombre": "E1", "peso": 5, "calorias": 3},
        {"nombre": "E2", "peso": 3, "calorias": 5},
        {"nombre": "E3", "peso": 5, "calorias": 2},
        {"nombre": "E4", "peso": 1, "calorias": 8},
        {"nombre": "E5", "peso": 2, "calorias": 3}
    ],
    "min_calories": 15,
    "max_weight": 10
}
Response (JSON):

{
    "la mejor combinacion es": ["E2", "E4", "E5"],
    "best_combination": [
        {"nombre": "E2", "peso": 3, "calorias": 5},
        {"nombre": "E4", "peso": 1, "calorias": 8},
        {"nombre": "E5", "peso": 2, "calorias": 3}
    ],
    "top_3_combinations": [
        {
            "elements": [
                {"nombre": "E2", "peso": 3, "calorias": 5},
                {"nombre": "E4", "peso": 1, "calorias": 8},
                {"nombre": "E5", "peso": 2, "calorias": 3}
            ],
            "total_weight": 6,
            "total_calories": 16
        }
    ]
}

--Persistencia de Datos
Actualmente, se utiliza SQLite para la persistencia, ya que la aplicación es sencilla. Sin embargo, para proyectos más grandes, se recomienda PostgreSQL.

--Configuración en settings.py para PostgreSQL (asegurarse que la base de datos este creada en postgresql previamenete isntalada y configurada)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mydatabase",
        "USER": "mydatabaseuser",
        "PASSWORD": "mypassword",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

--Escalabilidad y Despliegue
Para escalar la aplicación y facilitar su despliegue, se recomienda Dokku en un Droplet de DigitalOcean.

Ventajas de Dokku:
- Configuración sencilla de proxy y Nginx.
- Almacenamiento intuitivo.
- Manejo de variables de entorno para mantenerlas seguras.
- Despliegue con Dockerfile o Procfile para manejar múltiples contenedores.

Servicios recomendados para escalabilidad:
* Redis / RabbitMQ / Celery → Para tareas asíncronas y procesamiento en segundo plano.
* Postgresql → dokku tiene un plugin de postgresql para gestionar contenedor de postgresql en servidor
* Frontend en ReactJS o SolidJS → Para una mejor experiencia de usuario.

Contacto
Email   : ncyl91@gmail.com
LinkedIn: linkedin.com/in/ncyl91/
GitHub  : github.com/NiengLee