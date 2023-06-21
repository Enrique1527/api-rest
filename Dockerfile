# Define la imagen base
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt .
COPY app.py .
COPY config.py .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que se ejecuta la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD [ "python", "app.py" ]