#user can choose whether they want pickup or delivery

#bugs

print ("Do you want your magical drink to be picked up or delivered?")

print ("For pickup, please enter '1'")
print ("For delivery, please enter '2'")

low = 1 #repesents that lowest input is 1
high = 2 #represents that highest input is 2

while True:
    try:
        delivery = int(input ("Please enter a number ≧ ◠ ᴥ ◠ ≦  ")) #int for integer input 
        if delivery >= 1 and delivery <= 2:
            if delivery == 1:
                print ("You have chosen to pickup your order （っ＾▿＾)っ♥") #prints this message if typed 2
                break
    
            elif delivery == 2:
                print ("You have chosen delivery for today ʕ•́ᴥ•̀ʔ") #prints this message if typed 1
                break
    
        else:
            print("Number must be '1' or '2'")
    except ValueError: 
        print ("Sorry, that was an invalid input ( > ⌂ < ) ") #prints this message if input entered incorrectly"
        print ("Please enter 1 or 2")