#Jarra Piatos- Barista chatbot program: Digital Assessment Term 1

from random import randint #random intiger (random number generator)

#list of randomly generated names
names = ["Zunalora", "Kyzumath", "Malos", "Manazyri", "Zycandos", "Cornelius", "Aquilla", "Lelaine", "Doriath", "Zephyr"]

#Welcome message with random name
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

#Menu for pickup or delivery




#Pickup information - name and phone number




#Delivery infromation - name, address and phone




#Choose total number of drinks - maximum 5 drinks per customer




#Drinks menu




#Drinks order from menu - print each drink order with cost




#Print order out - including if order is delivery or pickup - names and price of each drink - total cost including any delivery charge




#Ability to cancel or proceed with the order




#Option for new order or to exit




#Main function
def main():
    '''
    Purpose: to run all functions
    Parameters: none
    Returns: None
    '''
    welcome()

main()