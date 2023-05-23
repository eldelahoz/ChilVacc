# ChilVacc interfaz 

## Instalar las dependencias del proyecto

### `npm install`  

## Iniciar el  proyecto

Tu puedes correr el proyecto con:

### `npm start`

## Dockerizar

Para poder tener un conedor de la app, tenemos que generar la imagen

`docker build -t "nombre de la imagen" .`

Luego generar un contenedor de esa imagen

`docker run --name "nombre del contenedor" -p 3000:3000 "nombre de la imagen"`

Y tendremos nuestro frontend dockerizado

Lo puedes observar en tu navegador en [http://localhost:3000](http://localhost:3000).

# Documentacion 

https://create-react-app.dev/docs/getting-started

# Introducción a Create React App 

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).
