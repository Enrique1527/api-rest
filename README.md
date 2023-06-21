Requisitos:
Python 3.x
Flask
Flask-MySQLdb

Instalación:
Clona el repositorio en tu máquina local.
Asegúrate de tener Python 3.x instalado en tu sistema.
Instala las dependencias ejecutando el siguiente comando en tu terminal:
pip install flask flask-mysqldb


Configuración:
Abre el archivo config.py y verifica la configuración de la base de datos MySQL. 
Asegúrate de que los valores de MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD y MYSQL_DB coincidan con tu entorno de desarrollo.
Guarda los cambios en el archivo config.py.

Buscar película por título:
URL: /peliculas/title/{title}
Método: GET
Descripción: Busca una película por su título en la base de datos.
Parámetros de ruta:
{title}: Título de la película a buscar.

Buscar películas por año:
URL: /peliculas/year/{year}
Método: GET
Descripción: Busca todas las películas que se produjeron en un año específico en la base de datos.
Parámetros de ruta:
{year}: Año de producción de las películas a buscar.
Respuesta exitosa:
Código: 200 (OK)


Registrar una nueva película: 
URL: /peliculas/registrar
Método: POST
Descripción: Registra una nueva película en la base de datos.
Parámetros en el cuerpo de la solicitud (JSON):
title: Título de la película (cadena).
year: Año de lanzamiento de la película (cadena).
summary: Resumen de la película (cadena).
short_summary: Resumen corto de la película (cadena).
imdb_id: ID de IMDB de la película (cadena).
runtime: Duración de la película (cadena).
youtube_trailer: Enlace al tráiler de la película en YouTube (cadena).
raiting: Calificación de la película (cadena).
movie_poster: Enlace al póster de la película (cadena).
director: Director de la película (cadena).
writers: Guionistas de la película (cadena).
cast: Elenco de la película (cadena).
Respuesta exitosa:
Código: 200 (OK)

Actualizar información de una película: 
URL: /peliculas/actualizar/{imdb_id}
Método: PUT
Descripción: Actualiza la información de una película en la base de datos utilizando su ID de IMDB.
Parámetros de ruta:
{imdb_id}: ID de IMDB de la película a actualizar.
Parámetros en el cuerpo de la solicitud (JSON): Los mismos parámetros que para registrar una nueva película.
Respuesta exitosa:
Código: 200 (OK)

Manejo de errores:
La API maneja el error 404 (Página no encontrada) y muestra un mensaje de error correspondiente.
