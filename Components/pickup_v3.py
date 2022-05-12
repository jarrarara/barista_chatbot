customer_details = {} #customer details dictionary

print("Please enter your pickup information (*＾▽＾)")

#customer name
valid = False
while not valid: 
    customer_details ["name"] = input("Please state your name on the space prodided: ")
    if customer_details ["name"] != "":
        print(customer_details ["name"])
        break #breaks the 'asking for name" cycle out of the loop
    else:
        print("Sorry, this cannot be left blank ( T ^ T )")

#customer phone
valid = False
while not valid: 
    customer_details ["phone"] = input("Please enter your phone number on the space provided: ")
    if customer_details ["phone"] != "":
        print(customer_details ["phone"])
        break #breaks the 'asking for phone number" cycle out of the loop
    else:
        print("Sorry, this cannot be left blank ( T ^ T )")
        
print (customer_details)