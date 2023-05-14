from fastapi import FastAPI
import MainBot
from pydantic import BaseModel

app = FastAPI()

class MensajeBot(BaseModel):
    mensaje: str

@app.get('/')
def hello_world():
    return 'Hello world!'


@app.post('/')
def respuesta_bot(mensaje: MensajeBot):
    return MainBot.mainBot(mensaje.mensaje)