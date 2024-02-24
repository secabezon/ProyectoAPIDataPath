Descripción de archivos principales del repositorio

1. main.py Ejecuta la aplicación con las funciones declaras en el archivo route.py
2. route.py Se enlistan todas las funcionalidades de la API
3. movie_controller.py Se codifica y especifica todas las funcionalidades y metodos que posee la API
4. Model.py Se Define el esquema de los datos que debe recibir y entregar la API, este servirá para la comunicación con MySQL
5. requeriments.txt Se enlistan todas las librerias necesarias para la ejecución del proyecto

Descripción General del proyecto

Se genera dentro de este repositorio un proyecto que tiene como fin la generación de una API que sea capaz de conectarse a un contenedor que posea MySQL y dentro de esta, pueda guardar datos sobre peliculas. Para esto se generan archivos Python que definen los distintos metodos, funcionalidades y esquemas que debe poseer los datos al momento de interactuar con MySQL.

Despliegue para una API Básica - Dockerizada (GET, POST, PUT, DELETE)

Esta guía te llevará a través del proceso de construir una API básica con operaciones crear, leer, actualizar y eliminar, usando contenedores Docker. La API interactuará con una base de datos MySQL.

Requisitos previos
Docker: Asegúrate de tener Docker instalado en tu sistema.

Pasos
1. Abrir una Terminal
Abre una terminal en tu máquina.

2. Navegar hasta la Carpeta del Proyecto
Cambiar al directorio que contiene tu proyecto de API.

cd ruta/proyecto

3. Construir la Imagen Docker
Construye la imagen Docker para tu API.

docker build -t dockerfile .

4. Descargar la Imagen de MySQL
Descarga la imagen de MySQL para crear un contenedor para la base de datos.

docker pull mysql

5. Ejecutar el Contenedor de la API
Ejecuta el contenedor de la API, indicando el puerto 8080 de tu máquina al puerto 80 del contenedor.

docker run -p 8080:80 dockerfile nombre_contenedor

6. Ejecutar el Contenedor de Mysql
Ejecuta el contenedor del Mysql, indicando el puerto 3307 de tu máquina al puerto 3306 del contenedor.

docker run -p 3307:3306 dockerfile mysql

7. Crear una Red Docker
Crea una red Docker para mejorar la comunicación entre el contenedor de MySQL y el contenedor de la API.

docker network create appapi
docker network connect appapi mysql
docker network connect appapi nombre_contenedor


Ahora, tu contenedor de API y el contenedor de MySQL están conectados a través de la red appapi.

8. Probar la API con Postman
Se consulta las funciones básicas desde Postman:

Petición GET
URL: http://localhost:8080/my_collections
Método: GET

Petición POST
URL: http://localhost:8080/my_collections
Método: POST
Body: {"Autor": "datos1", "Descripcion": "datos2", "FechaEstreno": "01/01/2023"}

Petición PUT
URL: http://localhost:8080/my_collections/1
Método: PUT
Body: {"Autor": "datos1", "Descripcion": "datos2", "FechaEstreno": "01/01/2023"}

Petición DELETE
URL: http://localhost:8080/my_collections/1
Método: DELETE
