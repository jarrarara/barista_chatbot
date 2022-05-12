customer_details = {} #customer details dictionary

def not_blank(question): #'question' parameter becomes the question from basic information
    valid = False
    while not valid:
        response = input(question)
        if response != "": #if the input is not blank it returns to print the entered customer details
            return response
        else: #if the input is blank, prints the response below then asks the 'question' again
            print("Sorry, this cannot be left blank ( T ^ T )")

#name basic information
question = ("Please enter your name on the space provided (*＾▽＾): ")
#customer name
customer_details ["name"] = not_blank(question)
#prints the entered customer details
print (customer_details["name"])

#phone number basic information
question = ("Please enter your phone number on the space provided (☆ ^ __ ^ ☆): ")
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