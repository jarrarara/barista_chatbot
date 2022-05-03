from random import randint #random intiger (random number generator)

#list of randomly generated names
names = ["Zunalora", "Kyzumath", "Malos", "Manazyri", "Zycandos", "Cornelius", "Aquilla", "Lelaine", "Doriath", "Zephyr"]

def welcome(): #defines fuction welcome
    '''
    Purpose: to generate a random name from the list and print a welcome message to the user
    Parameters: none
    Returns: None
    '''
    num = randint(0,9) #picks out random names to generate in the code
    name = (names[num])
    print("o()xx[{:::::::::::::::: Welcome to Cafe Encantadia :::::::::::::>") #prints the welcome message along with the randomly generated name
    print("✧─ ･ ｡ﾟ★: *.✦ .* :★. ─✧ My name is", name, "✧─ ･ ｡ﾟ★: *.✦ .* :★. ─✧")
    print("I will be asissting you for today. How may I help our dear costumer? ( ✿ ◠ ‿ ◠ )")

def main():
    '''
    Purpose: to run all functions
    Parameters: none
    Returns: None
    '''
    welcome()

main()