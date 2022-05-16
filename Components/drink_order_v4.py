#asks for how many drinks the user wants to order
#list of drink names
drink_names = ['Heart of the City','Golden Eden','Night of Swirling Stars','Moonlit Alley','Foamy Reef','Scholar Afternoon',
            'Brightcrown','Laughter and Cheer','Misty Garden','Love Poem','Sweet Cider Kiss','Dawning Dew','Gray Valley Sunset','Snow-Covered Kiss']

#list of prices of drinks
drink_prices = ['6.50','6.50','6.50','6.50','7.50','7.50','7.50','7.50','8.00','8.00','8.00','8.00','9.00','9.00'] 

#list to store ordered drinks
order_list = []
#list store drink prices
order_cost = []

def menu(): #function for running the drinks menu selection and prices
    num_drinks = 14

    for count in range (num_drinks):
        print("{} {} ${}" .format(count+1, drink_names[count], drink_prices[count])) #prints the drinks names and the drink price together in menu format
        #+1 starts the count at 1 and not 0



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
        
menu()
order_drinks()