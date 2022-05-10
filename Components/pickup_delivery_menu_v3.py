#user can choose whether they want pickup or delivery

#bugs
#invalid input triggers else statement but program does not ask for input again

print ("Do you want your special drink to be picked up or delivered?")

print ("For pickup, please enter '1'")
print ("For delivery, please enter '2'")

delivery = input ()

if delivery == 1:
    print ("You have chosen to pickup your order （っ＾▿＾)っ♥") #prints this message if typed 2
    
elif delivery == 2:
    print ("You have chosen delivery for today ʕ•́ᴥ•̀ʔ") #prints this message if typed 1
    
else: 
    print ("Sorry, that was not a valid input ( > ⌂ < ) ")