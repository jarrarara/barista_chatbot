#Jarra Piatos- Barista chatbot program: Digital Assessment Term 1

import random #libary that is within python
from random import randint #random intiger (random number generator)

#list of randomly generated names
names = ["Zunalora", "Kyzumath", "Malos", "Manazyri", "Zycandos", "Cornelius", "Aquilla", "Lelaine", "Doriath", "Zephyr"]

num = randint(0,9) #picks out random names to generate in the code
name = (names[num])

print(name) #prints the name thats is randomly generated

