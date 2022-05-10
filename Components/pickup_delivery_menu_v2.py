#user can choose whether they want pickup or delivery

#bugs
#will only work for valid input "d" and "p"
#invalid input triggers else statement but program does not ask for input again

print ("Do you want your special drink to be picked up or delivered?")

print ("For delivery, please enter 'd'")
print ("For pickup, please enter 'p'")

delivery = input ()

if delivery == "d":
    print ("You have chosen delivery for today ʕ•́ᴥ•̀ʔ")
    
elif delivery == "p":
    print ("You have chosen to pickup your order （っ＾▿＾)っ♥ ")
    
else: 
    print ("Sorry, that was not a valid input ( > ⌂ < ) ")