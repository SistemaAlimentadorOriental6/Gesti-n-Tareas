# Sistema de Gestión de Tareas

Este proyecto es una aplicación web desarrollada con **Django**, diseñada para facilitar la gestión de tareas en la organización mediante comités o reuniones.


## Características principales
- 📁 **Gestión de Comités**: Creación y administración de comités.
- ✅ **Asignación de Tareas**: Cada comité puede tener múltiples tareas asignadas, con un responsable por tarea.
- 🔁 **Jerarquía de Tareas**:
  - Tareas principales
  - Subtareas
  - Subtareas adicionales (hijas de las subtareas)
- ✍️ **Gestión de Estados**: El usuario gestor del sistema puede crear, modificar o cambiar el estado de cualquier tarea, subtarea o subtarea adicional.
- 📤 **Generación y Envío de Reportes**:
  - El sistema permite exportar a **Excel** el listado completo de tareas, subtareas y subtareas adicionales de un comité seleccionado.
  - Cada responsable recibe automáticamente un correo con el Excel personalizado, que contiene **solo las tareas que le han sido asignadas**. 

## Arquitectura del Sistema
El sistema está desarrollado con el framework **Django** siguiendo el patrón **Model-Template-View (MTV)**:
- **Modelos**: Representan la estructura de la base de datos mediante el ORM de Django.
- **Vistas**: Gestionan la lógica del negocio y la interacción con los modelos.
- **Plantillas**: Manejan la presentación con HTML, CSS y Bootstrap.

## Tecnologías utilizadas
- **Backend**: Django 5.2.3, Django Templates, Django ORM, Asgiref 3.8.1, sqlparse 0.5.3
- **Frontend**: Bootstrap, HTML5, CSS3, JavaScript, AJAX
- **Base de Datos**: MySQL con mysqlclient y pyodbc
- **Seguridad**: Middleware de Django, autenticación y protección CSRF
- **Manejo de archivos**: Configuración de archivos estáticos y multimedia con tzdata

## Estructura del Proyecto
El proyecto se organiza en carpetas siguiendo la estructura de Django:
```
admintaskG/
│── Public/
    │── css/
    │── img/
    │── js/
│── Templates/
    │── Comites/
    │── Inc/
    │── Login/
    │── partials/
    │── Login/
    │── pdf/
    │── Subtareas/
    │── SubtareasAdicionales/
    │── Tareas/
    │── base.html
│── __init__.py
│── asgi.py
│── models.py
│── settings.py
│── urls.py
│── views.py
│── wsgi.py
│── env/
│── .env
│── gitignore
│── manage.py
│── README.md
│── requirements.txt
```

## Base de Datos
El sistema gestiona los registros de las salidas mediante las siguientes tablas principales:
- `comite`: Almacena la información del comité creado.
- `tarea`: Almacena la tarea creada con el comité asociado y el responsable asignado.
- `sub_tarea`: Almacena la subtarea creada con la tarea asociada y el responsable asignado.
- `subtarea_adicional`: Almacena la subtarea adicional creada con la subtarea asociada y el responsable asignado.


### Creación de la Base de Datos
```sql
CREATE DATABASE gestiontareas;

USE gestiontareas;

CREATE TABLE IF NOT EXISTS `comite` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descripcion_comite` varchar(100) NOT NULL,
  `creador_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `creador_id` (`creador_id`)
)


CREATE TABLE IF NOT EXISTS `tarea` (
  `id` int NOT NULL AUTO_INCREMENT,
  `estado` int NOT NULL,
  `comite_id` int DEFAULT NULL,
  `descripcion_tarea` varchar(200) NOT NULL,
  `responsable` varchar(100) NOT NULL,
  `correo_responsable` varchar(250) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_cierre` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `comite_id` (`comite_id`)
)


CREATE TABLE IF NOT EXISTS `sub_tarea` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descripcion_subtarea` varchar(200) NOT NULL,
  `estado` int NOT NULL,
  `tarea_id` int DEFAULT NULL,
  `responsable` varchar(100) NOT NULL,
  `correo_responsable` varchar(250) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_cierre` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tarea_id` (`tarea_id`)
)

  CREATE TABLE IF NOT EXISTS `subtarea_adicional` (
    `id` int NOT NULL AUTO_INCREMENT,
    `descripcion_subtarea_adicional` varchar(200) NOT NULL,
    `estado` int NOT NULL,
    `subtarea_id` int DEFAULT NULL,
    `responsable` varchar(100) NOT NULL,
    `correo_responsable` varchar(250) NOT NULL,
    `fecha_inicio` date NOT NULL,
    `fecha_cierre` date DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `subtarea_id` (`subtarea_id`)
  ) 


```

## Respaldo de la Información
Se recomienda realizar backups cada 15 días (o semanalmente si hay un alto volumen de registros) para garantizar la seguridad de la información.

## Instalación y Configuración
1. Clona el repositorio:
   ```bash
   git clone https://github.com/JhonatanUsugaSao6/Gestion-tareas-.git
   ```
2. Instala las dependencias:
   ```bash
   SECRET_KEY = tu-clave-seguridad

    DEBUG = True o False

    ALLOWED_HOSTS = localhost, 127.0.0.1

    # Base de datos MySQL (Default)
    ENGINE_MYSQL=tu-engine
    NAME_MYSQL=tu-tabla
    USER_MYSQL=tu-usuario
    PASSWORD_MYSQL=tu-contraseña
    HOST_MYSQL=tu-host
    PORT_MYSQL=tu-puerto
    INIT=SET sql_mode='STRICT_TRANS_TABLES'
   ```

3. Crear archivo .env:
   ```bash
   pip install -r requirements.txt
   ```

4. Realiza las migraciones de la base de datos:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```



