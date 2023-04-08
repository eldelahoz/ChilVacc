import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy
import tflearn 
import tensorflow
import json
import random
import pickle 
import discord
llave = "MTA5NDAzNDM5MTMxNzEwMjgyMw.GwEYCn.vKCizLAFHO5Onn_i6VjJBr83RrUewP4_-EWFH0"

nltk.download('punkt')
with open('contenido.json', encoding='utf-8') as archivo:
    datos = json.load(archivo)

try:
    with open("variable.pickle", "rb") as archivoPickle:
        palabras, tags, entrenamiento, salida = pickle.load(archivoPickle)
except:
    palabras=[]
    tags=[]
    auxX=[]
    auxY=[]

    for contenido in datos["contenido"]:
        for patrones in contenido["patrones"]:
            auxPalabra = nltk.word_tokenize(patrones)
            palabras.extend(auxPalabra)
            auxX.append(auxPalabra)
            auxY.append(contenido["tag"])

            if contenido ["tag"] not in tags:
                tags.append(contenido["tag"])

    palabras = [stemmer.stem(w.lower()) for w in palabras if w!="*"]
    palabras = sorted(list(set(palabras)))
    tags = sorted(tags)

    entrenamiento=[]
    salida=[]
    salidaVacia=[0 for _ in range(len(tags))]

    for x, documento in enumerate(auxX):
        cubeta=[]
        auxPalabra=[stemmer.stem(w.lower())for w in documento]
        for w in palabras:
            if w in auxPalabra:
                cubeta.append(1)
            else:
                cubeta.append(0)
        filaSalida=salidaVacia[:]
        filaSalida[tags.index(auxY[x])]=1
        entrenamiento.append(cubeta)
        salida.append(filaSalida)
        entrenamiento=numpy.array(entrenamiento)
        salida=numpy.array(salida)
        with open("variable.pickle", "wb") as archivoPickle:
            pickle.dump((palabras, tags, entrenamiento, salida),archivoPickle)


tensorflow.compat.v1.reset_default_graph()
red=tflearn.input_data(shape=[None,len(entrenamiento[0])])
red=tflearn.fully_connected(red,10)
red=tflearn.fully_connected(red,10)
red=tflearn.fully_connected(red,len(salida[0]), activation="softmax")
red=tflearn.regression(red)

modelo=tflearn.DNN(red)
try:
    modelo.load("modelo.tflearn")
except:
    modelo.fit(entrenamiento, salida, n_epoch=1000,batch_size=10, show_metric=True)
    modelo.save("modelo.tflearn")

def mainBot():
    global llave
    intents = discord.Intents.default()
    intents.message_content = True
    cliente = discord.Client(intents=intents)
    while True:
        @cliente.event
        async def on_message(mensaje):
            if mensaje.author == cliente.user:
                return
            cubeta = [0 for _ in range(len(palabras))]
            entradaProcesada = nltk.word_tokenize(mensaje.content)
            entradaProcesada = [stemmer.stem(palabra.lower()) for palabra in entradaProcesada]
            for palabraIndividual in entradaProcesada:
                for i,palabra in enumerate(palabras):
                    if palabra == palabraIndividual:
                        cubeta[i] = 1
            resultados = modelo.predict([numpy.array(cubeta)])
            resultadosIndices = numpy.argmax(resultados)
            tag = tags[resultadosIndices]

            for tagAux in datos["contenido"]:
                if tagAux["tag"] == tag:
                    respuesta = tagAux["respuestas"]
            ##print("BOT: ", random.choice(respuesta))
            await mensaje.channel.send(random.choice(respuesta))
        cliente.run(llave)
mainBot()
