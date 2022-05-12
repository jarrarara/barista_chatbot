#Jarra Piatos- Barista chatbot program: Digital Assessment Term 1

import random #libary that is within python
from random import randint #random intiger (random number generator)

#list of randomly generated names
names = ["Zunalora", "Kyzumath", "Malos", "Manazyri", "Zycandos", "Cornelius", "Aquilla", "Lelaine", "Doriath", "Zephyr"]

customer_details = {} #customer details dictionary

#validates input if they are blank
def not_blank(question): #'question' parameter becomes the question from basic information
    valid = False
    while not valid:
        response = input(question)
        if response != "": #if the input is not blank it returns to print the entered customer details
            return response.title() #makes the first letter of every word a capital letter
        else: #if the input is blank, prints the response below then asks the 'question' again
            print("Sorry, this cannot be left blank ( T ^ T )")
            
#Welcome message with random name
#defines fuction welcome
def welcome(): 
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
def order_type(): 
    print ("Do you want your magical drink to be picked up or delivered?")

    print ("For pickup, please enter '1'")
    print ("For delivery, please enter '2'")

    low = 1 #repesents that lowest input is 1
    high = 2 #represents that highest input is 2

    while True:
        try:
            delivery = int(input ("Please enter a number ≧ ◠ ᴥ ◠ ≦ :  ")) #int for integer input 
            if delivery >= 1 and delivery <= 2: #makes sure that only numbers more than 1 or equal to 1 and more less than or equal to 2 can only be input
                if delivery == 1:
                    print ("You have chosen to pickup your order （っ＾▿＾)っ♥") #prints this message if typed 2
                    pickup() #if chosen pickup, will print pickup input information
                    break #breaks the 'asking if pickup or delviery" cycle out of the loop
        
                elif delivery == 2:
                    print ("You have chosen delivery for today ʕ•́ᴥ•̀ʔ") #prints this message if typed 1
                    break #breaks the 'asking if pickup or delviery" cycle out of the loop
        
            else:
                print("Number must be '1' or '2'") #prints messgae if any other number other than 1 or 2 is typed
        except ValueError: 
            print ("Sorry, that was an invalid input ( > ⌂ < ) ") #prints this message if input entered incorrectly"
            print ("Please enter 1 or 2")

#Pickup information - name and phone number
#name basic information
def pickup():
    question = ("Please enter your name on the space provided (*＾▽＾): ")
#customer name
    customer_details ["name"] = not_blank(question)
#prints the entered customer details
    print (customer_details["name"])

#phone number basic information
    question = ("Please enter your phone number on the space provided (*＾▽＾): ")
#customer phone number
    customer_details ["phone"] = not_blank(question)
#prints the entered customer details
    print (customer_details["phone"])


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
    order_type()


main()