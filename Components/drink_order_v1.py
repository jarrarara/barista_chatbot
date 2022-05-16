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

menu()

num_drink = 0

num_drink = int(input("How many drinks would our dear customer like to order o(〃＾▽＾〃)o? "))

print(num_drink)

#choose from drinks menu
print("Please choose the drinks you want by entering the corresponding number from our menu o(≧ ε ≦ o)")
for item in range(num_drink):
    while num_drink > 0: #if number input is greater than 0, runs the code below
        drinks_ordered = int(input()) #user inputs a number and the nu,mber gets stored in the order_list
        order_list.append(drink_names[drinks_ordered]) #order_list appends to the drink names at the top
        order_cost.append(drink_prices[drinks_ordered]) #order_list appends to the drink prices at the top
        num_drink = num_drink-1
        
print(order_list)
print(order_cost)
        

#countdown until all drinks they want are ordered

#print their order