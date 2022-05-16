#Jarra Piatos- Barista chatbot program: Digital Assessment Term 1

#menu that users can choose from and how many drinks they want
#list of drink names
drink_names = ['Heart of the City','Golden Eden','Night of Swirling Stars','Moonlit Alley','Foamy Reef','Scholar Afternoon',
            'Brightcrown','Laughter and Cheer','Misty Garden','Love Poem','Sweet Cider Kiss','Dawning Dew','Gray Valley Sunset','Snow-Covered Kiss']

#list of prices of drinks
drink_prices = ['6.50','6.50','6.50','6.50','7.50','7.50','7.50','7.50','8.00','8.00','8.00','8.00','9.00','9.00'] 

#list to store ordered drinks
order_list = []
#list store drink prices
order_cost = []

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
def welcome(): #function for the opening greeting of the user
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
def order_type(): #function for asking the user if they want pickup or delivery for their order
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
                    pickup_info() #if chosen pickup, will print pickup input information
                    break #breaks the 'asking if pickup or delviery" cycle out of the loop
        
                elif delivery == 2:
                    print ("You have chosen delivery for today ʕ•́ᴥ•̀ʔ") #prints this message if typed 1
                    delivery_info() #if chosen pickup, will print pickup input information
                    break #breaks the 'asking if pickup or delviery" cycle out of the loop
        
            else:
                print("Number must be '1' or '2'") #prints messgae if any other number other than 1 or 2 is typed
        except ValueError: 
            print ("Sorry, that was an invalid input ( > ⌂ < ) ") #prints this message if input entered incorrectly"
            print ("Please enter 1 or 2")

#Pickup information - name and phone number
#name basic information
def pickup_info():
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
def delivery_info():
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
#house number basic information
    question = ("Please enter your house number on the space provided (^_^)/: ")
#customer house number
    customer_details ["house"] = not_blank(question)
#prints the entered customer details
    print (customer_details["house"])

#street name basic information
    question = ("Please enter your street name on the space provided (^・ω・^): ")
#customer name
    customer_details ["street"] = not_blank(question)
#prints the entered customer details
    print (customer_details["street"])

#suburb basic information
    question = ("Please enter your suburb on the space provided (* ^ v ^ *): ")
#customer name
    customer_details ["suburb"] = not_blank(question)
#prints the entered customer details
    print (customer_details["suburb"])

#Drinks menu

def menu(): #function for running the drinks menu selection and prices
    num_drinks = 14

    for count in range (num_drinks):
        print("{} {} ${}" .format(count+1, drink_names[count], drink_prices[count])) #prints the drinks names and the drink price together in menu format
        #+1 starts the count at 1 and not 0

#Choose total number of drinks - maximum 6 drinks per customer/order
#Drinks order from menu - print each drink order with cost
def order_drinks():
    num_drink = 0
    while True:
        try:
            num_drink = int(input("How many drinks would our dear customer like to order o(〃＾▽＾〃)o? "))
            if num_drink >= 1 and num_drink <= 6: #restricts the number of drinks ordered by nothing less than 1 and nothing greater than 6
                break #breaks the while True loop above and moves on to the next function below
            else:
                print("Your drink orders cannot exceed the maximum of 6 and minimum of 1, sorry! \(￣^￣)")
        except ValueError: 
            print ("Sorry, that was an invalid input ( > ⌂ < ) ") #prints this message if input entered incorrectly"
            print ("Please enter 1 and 6") 
    #choose from drinks menu
    for item in range(num_drink):
        while num_drink > 0: #if number input is greater than 0, runs the code below
            while True:
                try:
                    drinks_ordered = int(input("Please choose the drinks you want by entering the corresponding number from our menu o(≧ ε ≦ o) "))
                    if drinks_ordered >= 1 and drinks_ordered <= 14: #restricts the number of drinks ordered by nothing less than 1 and nothing greater than 6
                        break #breaks the while True loop above and moves on to the next function below
                    else:
                        print("Your drink orders cannot exceed the maximum of 14 and minimum of 1, sorry! \(￣^￣)")
                except ValueError: 
                    print ("Sorry, that was an invalid input ( > ⌂ < ) ") #prints this message if input entered incorrectly"
                    print ("Please enter 1 and 14")
            drinks_ordered = drinks_ordered -1
            order_list.append(drink_names[drinks_ordered]) #order_list appends to the drink names at the top
            order_cost.append(drink_prices[drinks_ordered]) #order_list appends to the drink prices at the top
            print("{} ${}" .format(drink_names[drinks_ordered], drink_prices[drinks_ordered])) #prints the drinks names and the drink price together in menu format
            num_drink = num_drink-1 #removes the selected order from the menu



#Print order out - including if order is delivery or pickup - names and price of each drink - total cost including any delivery charge - essentially the reciept.




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
    menu()
    order_drinks()


main()