# ==== CONFIGURACION =====
# Usamos Node 18.16 alpine
FROM node:18.16.0-alpine
# Aplicamops la carpeta de trabajo que seria /app
WORKDIR /app
# Copiamos todos los archivos de nuestra carpeta
COPY . .
# ==== BUILD =====
# Instalamos todas las dependencias del proyecto
RUN npm install 
# Build la aplicacion
RUN npm run build
# ==== RUN =======
# Asignamos el entorno de produccion (Esto no estan necesario pero seria un ejemplo para asignar variables de entorno)
ENV NODE_ENV production
# Exponemos el puerto que va a usar la aplicaicon en este caso seria el 3000
EXPOSE 3000
# Iniciamos la aplicacion
CMD [ "npx", "serve", "build" ]