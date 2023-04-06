import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy
import tflearn 
import tensorflow
import json
import random
import pickle 

nltk.download('punkt')
with open('contenido.json') as archivo:
    datos = json.load(archivo)

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

palabras = [stemmer.stem(w.lower()) for w in palabras if w!="?"]
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

print(entrenamiento)
print(salida)