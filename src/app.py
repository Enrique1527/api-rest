from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import config

app=Flask(__name__)
conexion=MySQL(app)


#MUESTRA TODAS LAS PELICULAS DE LA BASE DE DATOS
@app.route('/peliculas', methods=['GET'])
def listar_peliculas():
    try:
        cursor=conexion.connection.cursor()
        sql="SELECT * FROM pelicula" #CONSULTA SQL
        cursor.execute(sql) #EJECUTA LA CONSULTA SQL
        datos=cursor.fetchall() #TRAE TODOS LOS REGISTROS
        peliculas=[] 
        for fila in datos:
            pelicula={'Titulo':fila[0], 
            'Año':fila[1], 
            'Summary':fila[2], 
            'Short_sumary':fila[3], 
            'IMDB_ID':fila[4], 
            'Runtime':fila[5],
            'Trailer Youtube':fila[6], 
            'Rating':fila[7], 
            'Movie poster':fila[8], 
            'Director':fila[9], 
            'Writers':fila[10], 
            'Cast':fila[11]}
            peliculas.append(pelicula)
        return jsonify({'Peliculas':peliculas, 'mensaje':"Peliculas listadas"})
        
    except Exception as ex:
        return jsonify({'mensaje': "Error"})



#BUSCAR UNA PELICULA POR SU NOMBRE
@app.route('/peliculas/title/<title>', methods=['GET'])
def leer_pelicula_title(title):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM pelicula WHERE title=%s"
        cursor.execute(sql, (title,))
        datos = cursor.fetchone()
        if datos is not None:
            pelicula = {
                'Titulo': datos[0], 
                'Año': datos[1], 
                'Summary': datos[2],
                'Short_sumary': datos[3], 
                'IMDB_ID': datos[4], 
                'Runtime': datos[5],
                'Trailer Youtube': datos[6], 
                'Rating': datos[7], 
                'Movie poster': datos[8],
                'Director': datos[9], 
                'Writers': datos[10], 
                'Cast': datos[11]
            }
            return jsonify(pelicula)  
        else:
            return jsonify({'mensaje': "Pelicula no encontrada"})  
    except Exception as ex:
        return jsonify({'mensaje': "Error"})



#BUSCAR TODAS LAS PELICULAS QUE SE PRODUJERON EN UN AÑO EN ESPECIFICO
@app.route('/peliculas/year/<year>', methods=['GET'])
def leer_pelicula_year(year):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM pelicula WHERE year='{0}'".format(year)
        cursor.execute(sql)
        datos = cursor.fetchall()
        if datos is not None:
            peliculas = []
            for fila in datos:
                pelicula = {
                    'Titulo': fila[0], 
                    'Año': fila[1], 
                    'Summary': fila[2],
                    'Short_sumary': fila[3], 
                    'IMDB_ID': fila[4], 
                    'Runtime': fila[5],
                    'Trailer Youtube': fila[6], 
                    'Rating': fila[7], 
                    'Movie poster': fila[8],
                    'Director': fila[9], 
                    'Writers': fila[10], 
                    'Cast': fila[11]
                }
                peliculas.append(pelicula)
            return jsonify({'Peliculas': peliculas}) 
        else:
            return jsonify({'mensaje': "No hay coincidencias"})  
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

#AGREGAR UNA NUEVA PELICULA
@app.route('/peliculas/registrar', methods=['POST'])
def registrar_pelicula():
    try:
        cursor = conexion.connection.cursor()
        # print(request.json)
        sql = """INSERT INTO pelicula (`title`, `year`, `summary`, `short_summary`, `imdb_id`, 
        `runtime`, `youtube_trailer`, `raiting`, `movie_poster`, `director`, `writers`, `cast`)
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}')""".format(
            request.json['title'],
            request.json['year'],
            request.json['summary'],
            request.json['short_summary'],
            request.json['imdb_id'],
            request.json['runtime'],
            request.json['youtube_trailer'],
            request.json['raiting'],
            request.json['movie_poster'],
            request.json['director'],
            request.json['writers'],
            request.json['cast']
        )
        cursor.execute(sql)
        conexion.connection.commit()
        cursor.close()
        return jsonify({'mensaje': "Pelicula registrada"})
    except Exception as ex:
        return jsonify({'mensaje': str(ex)})


#ACTUALIZAR UNA PELICULA PASANDO COMO PARAMETRO IMDB_ID PARA BUSCARLA
@app.route('/peliculas/actualizar/<imdb_id>', methods=['PUT'])
def actualizar_pelicula(imdb_id):
    try:
        cursor = conexion.connection.cursor()
        # print(request.json)
        sql = """UPDATE pelicula SET title='{0}',year='{1}',summary='{2}',
        short_summary='{3}',runtime='{4}',youtube_trailer='{5}',raiting='{6}',movie_poster='{7}',
        director='{8}',writers='{9}', cast='{10}' WHERE imdb_id='{11}'""".format(
            request.json['title'],
            request.json['year'],
            request.json['summary'],
            request.json['short_summary'],
            request.json['runtime'],
            request.json['youtube_trailer'],
            request.json['raiting'],
            request.json['movie_poster'],
            request.json['director'],
            request.json['writers'],
            request.json['cast'], imdb_id)
        cursor.execute(sql)
        conexion.connection.commit()
        cursor.close()
        return jsonify({'mensaje': "Pelicula actualizada"})
    except Exception as ex:
        return jsonify({'mensaje': "Error: " + str(ex)})



def pagina_no_encontrada(error):
    return "<h1>La pagina que intentas buscar no existe...</h1>",404

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()