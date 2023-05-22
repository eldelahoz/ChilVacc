#1.Importaciones:
import nltk #Importa la biblioteca NLTK (Natural Language Toolkit), utilizada para el procesamiento del lenguaje natural.
from nltk.stem.lancaster import LancasterStemmer 
stemmer = LancasterStemmer()#Se utiliza para realizar la stemización de palabras.
import numpy #Proporciona estructuras de datos y funciones para cálculos numéricos.
import tflearn #Es una capa de alto nivel construida sobre TensorFlow para facilitar la creación y entrenamiento de redes neuronales.
import tensorflow #Framework de aprendizaje automático utilizado como backend por tflearn.
import json #Se importa la biblioteca JSON para trabajar con datos en formato JSON.
import random # Se importa la biblioteca random para generar respuestas aleatorias.
import pickle # Se utiliza para serializar y deserializar objetos Python.

#2.Descarga de recursos de NLTK
#Descarga el recurso 'punkt' de NLTK, que es necesario para el tokenizado de texto.
nltk.download('punkt')

#3.Carga de datos
#Se el archivo JSON llamado 'contenido.json' en modo lectura y carga su contenido en 
#la variable datos. Este archivo debe contener los datos de entrenamiento para el chatbot, incluyendo patrones y respuestas asociadas 
with open('contenido.json', encoding='utf-8') as archivo:
    datos = json.load(archivo)

#4.Carga de datos previamente guardados
#Se intenta abrir y cargar los datos previamente procesados desde el archivo "variable.pickle". 
#Si el archivo no existe o hay algún error en la carga, se inicializan las variables necesarias como listas vacías.
try:
    with open("variable.pickle", "rb") as archivoPickle:
        palabras, tags, entrenamiento, salida = pickle.load(archivoPickle) #Estas variables almacenan los datos procesados necesarios para entrenar el modelo del chatbot.
except:
    #Se crean las listas vacias en las cuales posteriormente guardaremos las palabras ya separadas, tag, y dos listas
    #auxiliares mas para que nos ayudaran para terminar de dividir cada tag para la facil comprención del chatbots
    palabras=[]
    tags=[]
    auxX=[]
    auxY=[]

    for contenido in datos["contenido"]:
        for patrones in contenido["patrones"]:
            auxPalabra = nltk.word_tokenize(patrones)
            #Las palabras y las etiquetas se almacenan en listas y se eliminan duplicados.
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

    #5. Procesamiento de los datos
    #Se crea la estructura de datos necesaria para el entrenamiento del modelo. Cada patrón se representa como una lista de características binarias
    #donde 1 indica la presencia de una palabra en el patrón y 0 que esta no fue encontrada
    #esto haciendo uso de ordenamiento por cubeta
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
        #Los datos de entrenamiento se convierten en matrices NumPy para un procesamiento mas eficiente
        entrenamiento=numpy.array(entrenamiento)
        salida=numpy.array(salida)
        #6. Guardado de los datos procesados
        #Los datos procesados (palabras, etiquetas, entrenamiento y salida) se guardan en un archivo "variable.pickle" 
        # utilizando la biblioteca pickle para su uso posterior.
        with open("variable.pickle", "wb") as archivoPickle:
            pickle.dump((palabras, tags, entrenamiento, salida),archivoPickle)

#7.Configuración de la red neuronal
tensorflow.compat.v1.reset_default_graph() #Se resetea el gráfico predeterminado de TensorFlow.

#Se define la estructura de la red neuronal utilizando la API de tflearn. La red consta de una capa de entrada, dos capas 
#ocultas totalmente conectadas y una capa de salida con función de activación softmax
red=tflearn.input_data(shape=[None,len(entrenamiento[0])])
red=tflearn.fully_connected(red,10)
red=tflearn.fully_connected(red,10)
red=tflearn.fully_connected(red,len(salida[0]), activation="softmax")
red=tflearn.regression(red)

#Se define el objeto modelo utilizando la clase DNN de tflearn, que representa la red neuronal.
modelo=tflearn.DNN(red)

#8.Carga o entrenamiento del modelo
#Se intenta cargar el modelo previamente entrenado desde el archivo "modelo.tflearn". Si el archivo no existe o hay algún error 
#en la carga, se procede a entrenar el modelo utilizando los datos de entrenamiento.
try:
    modelo.load("modelo.tflearn")
except:
    #Durante el entrenamiento, se especifica el número de épocas (n_epoch), el tamaño del lote (batch_size) y se muestra la métrica de entrenamiento.
    modelo.fit(entrenamiento, salida, n_epoch=1000,batch_size=10, show_metric=True)
    modelo.save("modelo.tflearn")

#9. Función principal del chatbot
#La función mainBot() implementa un bucle infinito donde el chatbot espera la entrada del usuario.
def mainBot():
    while True:
        #La entrada del usuario se procesa separando el texto y realizando la asociación de las palabras.
        entrada = input("Tu: ")
        #Se crea un vector binario (cubeta) para representar la entrada del usuario.
        cubeta = [0 for _ in range(len(palabras))]
        entradaProcesada = nltk.word_tokenize(entrada)
        entradaProcesada = [stemmer.stem(palabra.lower()) for palabra in entradaProcesada]
        for palabraIndividual in entradaProcesada:
            for i,palabra in enumerate(palabras):
                if palabra == palabraIndividual:
                    cubeta[i] = 1
        #Se utiliza el modelo entrenado para predecir la etiqueta más probable para la entrada.
        resultados = modelo.predict([numpy.array(cubeta)])
        resultadosIndices = numpy.argmax(resultados)
        tag = tags[resultadosIndices]
        
        #Se selecciona una respuesta aleatoria asociada con la etiqueta predicha.
        for tagAux in datos["contenido"]:
            if tagAux["tag"] == tag:
                respuesta = tagAux["respuestas"]
        #La respuesta del chatbot se imprime.
        print("BOT: ", random.choice(respuesta))

#10. Llamada a la función principa
#El programa finaliza con la llamada a la función mainBot(), lo que inicia el chatbot y lo mantiene 
# en ejecución en un bucle infinito hasta que se interrumpa manualmente.
mainBot()