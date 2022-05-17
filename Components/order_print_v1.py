#prints out the ccustomer's order - a reciept
#list to store ordered drinks
order_list = ['Brightcrown','Laughter and Cheer','Misty Garden','Love Poem']
#list store drink prices
order_cost = ['7.50','7.50','7.50','8.00']

count = 0

for item in order_list:
    print("{} ${}" .format(item, order_cost[count]))
    count = count+1