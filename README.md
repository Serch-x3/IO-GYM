# IO-GYMS
IO-Gym es un software de administración de gyms, enfocado a ser una opción minimalista y sencilla de usar.

## Caracteristicas

## Instalación

### REQUISITOS DEL SISTEMA:

- Python 3.7 o superior
- Pip instalado (usualmente viene instalado junto con Python)
- Django 3.0.6            //pip install Django
- Mysql-connector-python    //pip install mysql-connector-python (se requiere tener instalado pip)
- django-filter            //pip install django-filter (se requiere tener instalado pip)
- django-daterange_filter        //pip install django-daterange-filter (se requiere tener instalado pip)
- widget_tweaks                     //pip install django-widget-tweaks (se requiere tener instalado pip)
- fernet_fields                     //pip install pip install django-fernet-fields (se requiere pip instalado)
- Mysqlclient            //pip install mysqlclient (se requiere tener instalado pip)


### PASOS DE INSTALACIÓN:

  1- Abra MySQL con el usuario con privilegios administrativos desde Consola o Terminal

  2- Ejecute el siguiente código SQL (encontrado en las primeras líneas del archivo SQLCODE.sql:
``` sql
        CREATE DATABASE IOGYM;
        GO
        CREATE USER 'djangoDB'@'localhost' IDENTIFIED BY 'AfterByte';
        GO
        GRANT ALL PRIVILEGES ON IOGYM.* TO 'djangoDB'@'localhost';
        USE IOGYM
```
  3- Abra la carpeta del proyecto desde Consola o Terminal y ejecute los siguientes comandos:  
``` python

        python manage.py makemigrations
        python manage.py migrate
      
```



  4- Navegue hasta el directorio donde se encuentra el programa y ejecute el código restante
    (en la terminal de MySQL con el usuario ‘root’ logueado y con la base de datos IOGYM en uso)
    contenido en el archivo /SQLCODE.sql con el comando source.


 5- Asegúrese que en la carpeta /clients/migrations sólo contenga el archivo 0001_initial.py.
Si se encuentra otro archivo además de estos, probablemente genere problemas para realizar las migraciones


6- Abra la carpeta del proyecto desde Consola o Terminal y ejecute los siguientes comandos
        
        python manage.py createsuperuser          //Crear una cuenta administrador
        python manage.py runserver


  7- Abra su navegador y acceda a la siguiente dirección:  
  http://localhost:8000

  Deberia abrir una nueva ventana con el Proyecto
  ## Docker
  Se incluye un docker-compose para poder correr en contendor la aplicación.
  ### Requerimientos
 - Docker
 - Docker-compose

Se crearan 2 contenedores
IOGYM-APP donde se continen la aplicacion.
IOGYM-DB Donde se localiza la base de datos.

1.- Crear el archivo docker.env con las siguientes varibles de entorno y ponerlo en la misma carpeta que el docker-compose
 
    MYSQL_ROOT_PASSWORD="DatabasePawsword"
    MYSQL_USER="djangoDB"
    MYSQL_PASSWORD="USERPASWORD"
    MYSQL_DATABASE="IOGYM"
modificando los dos password a su prefetencia.

2.- Ejecutar el siguiente comando en terminal
    
    docker-compose up -d 

3.- Una vez verificado que se creadon los contenedores entraremos al contenedor de la aplicacion:   

        docker exec -it IOGYM-APP bash
4.- Ejecutar el paso 3 de la instalacion

5.- Salir del contenedor con exit

6.- Ejecutar el siguiente comando

    docker exec -d IOGYM-DB mysql -u djangodb -p source SQLCODE.SQL

7.- La aplicacion debe estar funcionando


  ### FAQ
  #### Tengo ocupado el puerto 8000 puedo cambiarlo por otro?
  Si , al ejecutar el comando runserver se puede defirnir el puerto donde ejecutarlo con la siguiente sintaxis.

        python manage.py runserver 0.0.0.0:xxxx

Siendo XXXX el puerto donde se quiera ejecutar la aplicacion.

