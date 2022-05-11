print("Please enter your pickup information (*＾▽＾): ")

#customer name
valid = False
while not valid: 
    name = input("Please state your name on the space prodided: ")
    if name != "":
        print(name)
        break #breaks the 'asking for name" cycle out of the loop
    else:
        print("Sorry, this cannot be left blank ( T ^ T )")

#customer phone
valid = False
while not valid: 
    phone = input("Please enter your phone number on the space provided: ")
    if phone != "":
        print(phone)
        break #breaks the 'asking for phone number" cycle out of the loop
    else:
        print("Sorry, this cannot be left blank ( T ^ T )")