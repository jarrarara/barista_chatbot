#prints out the ccustomer's order - a reciept
#list to store ordered drinks
order_list = ['Brightcrown','Laughter and Cheer','Misty Garden','Love Poem']
#list store drink prices
order_cost = [7.50,7.50,7.50,8.00]

cust_details = {'name':'Viktor', 'phone':'09876542', 'house':'90', 'street':'Merryland', 'suburb':'Flatbush'} #test list

def print_order():
    print("Customer Details")
    print("\nCustomer Name: {} \nCustomer Phone: {} \nCustomer House number: {} \nCustomer Street Name: {} \nCustomer Suburb: {}" .format
    (cust_details['name'], cust_details['phone'], cust_details['house'], cust_details['street'], cust_details['suburb'])) #test list 2
    print() #prints nothing, acts as a breaker
    print("Order Details")
    count = 0
    for item in order_list:
        print("{} ${:.2f}" .format(item, order_cost[count])) #confirms the order and prints it in reciept format
        count = count+1
    print() #prints nothing, acts as a breaker
    total_cost = sum(order_cost)
    print(f"The total cost of your order is:${total_cost:.2f}" "!!" " o(* > ω < *)o") #prints the total cost of the order
    
    print_order()