import random #libary that is within python
from random import randint #random intiger (random number generator)

#list of randomly generated names
names = ["Zunalora", "Kyzumath", "Malos", "Manazyri", "Zycandos", "Cornelius", "Aquilla", "Lelaine", "Doriath", "Zephyr"]

num = randint(0,9) #picks out random names to generate in the code
name = (names[num])

print("o()xx[{:::::::::::::::: Welcome to Cafe Sephiroth :::::::::::::>") #prints the welcome message along with the randomly generated name
print("✧─ ･ ｡ﾟ★: *.✦ .* :★. ─✧ My name is", name, "✧─ ･ ｡ﾟ★: *.✦ .* :★. ─✧")
print("I will be asissting you for today. How may I help our dear costumer? ( ✿ ◠ ‿ ◠ )")