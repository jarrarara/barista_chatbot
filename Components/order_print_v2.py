#prints out the ccustomer's order - a reciept
#list to store ordered drinks
order_list = ['Brightcrown','Laughter and Cheer','Misty Garden','Love Poem']
#list store drink prices
order_cost = ['7.50','7.50','7.50','8.00']

cust_details = {'name':'Viktor', 'phone':'09876542', 'house':'90', 'street':'Merryland', 'suburb':'Flatbush'}

#print("\n", cust_details['name'], "\n", cust_details['phone'], "\n", cust_details['house'], "\n", cust_details['street'], "\n", cust_details['suburb'])

print("\n Customer Name:{} \n Customer Phone:{} \n Customer House number:{} \n Customer Street Name:{} \n Customer Suburb:{}" .format( cust_details['name'], 
cust_details['phone'], cust_details['house'], cust_details['street'], cust_details['suburb']))

count = 0
for item in order_list:
    print("{} ${}" .format(item, order_cost[count]))
    count = count+1