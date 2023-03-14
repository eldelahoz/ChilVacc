# Creación de entorno VirtualPython

```sh
# Para el entorno virtual es necesario usar una terminal
# (Puede ser la de preferencia o Gitbash)

python3 -m venv ChilVacVenv

# Para activar el entorno utilizamos el siguiente comando:
# Windows
source ChilVacVen/Scripts/activate
# Linux
source ChilVacVenv/bin/activate

# Luego instalamos los requerimentos con el siguiente comando:
pip install -r requirements.txt

# Ya con esto podemos correr nuestro servidor de FastAPI
uvicorn main:app -reload
```
