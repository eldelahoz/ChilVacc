# ChilVacc

[<img src="img/ChilVacc.png" width="250" height="250">](https://github.com/eldelahoz/ChilVacc)

## Gestion del Proyecto en Jira

[Jira ChilVac](https://chill-vacc.atlassian.net/jira/software/projects/CHIL/boards/1/roadmap)

## ChatBot

Se realiza un chatbot empleado librerías como nltk, tensorflow, entre otras para tener un chatbot por medio de un árbol de decisiones y una pequeña red neuronal para irlo entrenando.

### Usar el ChatBot

[ChatBot](https://github.com/eldelahoz/ChilVacc/tree/Entrega2/ChatBot)

Primero, crear el entorno virtual de Python:

```sh
# Terminal de Windows o Linux
python -m venv venv
# Para activar el entorno utilizamos el siguiente comando:
# Windows
source venv/Scripts/activate
# Linux
source venv/bin/activate
```

Segundo, instalar las librerías requeridas para el funcionamiento de la APP:

```sh
# Estar en la ruta de la carpeta ChatBot
pip install -r requirements.txt
```

Tercero, ejecutar la aplicacion:

```sh
# Estar en la ruta de la carpeta ChatBot
python MainBot.py
```
