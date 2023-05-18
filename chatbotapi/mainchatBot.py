import nltk
from nltk.chat.util import Chat, reflections
import re
import random


class MyChat(Chat):

    def __init__(self, pairs, reflections={}):

        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()

    def respond(self, str):

        for (pattern, response) in self._pairs:
            match = pattern.match(str)

            # did the pattern match?
            if match:
                resp = random.choice(response)  # pick a random response
                resp = self._wildcards(resp, match)  # process wildcards

                # fix munged punctuation at the end
                if resp[-2:] == "?.":
                    resp = resp[:-2] + "."
                if resp[-2:] == "??":
                    resp = resp[:-2] + "?"
                return resp


pairs = [
    ["Hi im (.*)", ["hello %1, What can I do for you?"]],
]


if __name__ == "__main__":
    print("Mi nombre es ChilVaccBot en que te puedo ayudar?")
    chat = Chat(pairs, reflections)
    user_input = input("> ")
    while(user_input != "salir"):
        reponse = chat.respond(user_input)
        print(reponse) if (reponse is not None) else print("No entendiendo tu pregunta, por favar verifica si es referente al tema de vacunación")
        user_input = input("> ")

