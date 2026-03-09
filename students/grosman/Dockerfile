#Imagen base
FROM python:3.12-alpine

#defino el directorio de trabajo
WORKDIR /app

#crea usuario sin privilegios
RUN addgroup -S app && adduser -S app -G app

#copio las dependencias en el directorio de trabajo
COPY requirements.txt .

#instalo las dependencias, sin guardar el cache para reducir espacio
RUN pip install --no-cache-dir -r requirements.txt

#copio el codigo de mi app al directorio de trabajo
COPY app.py .

#crea la carpeta de logs y le da permisos al usuario que se creo previamente para poder escribir visitas.log
RUN mkdir -p /var/log/app && chown -R app:app /var/log/app

#el proceso corre como usuario no root
USER app

#documenta que la app expone este puerto, pero no lo expone 
EXPOSE 8080

#docker verifica cada cierto tiempo que la aplicacion este health, si no la marca como un healthy
HEALTHCHECK --interval=10s --timeout=3s --retries=5 \
  CMD wget -qO- http://localhost:8080/health >/dev/null || exit 1

# corre la app 
CMD ["python","/app/app.py"]