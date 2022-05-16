#menu that users can choose from and how many drinks they want
drink_names = ['Heart of the City','Golden Eden','Night of Swirling Stars','Moonlit Alley','Foamy Reef','Scholar Afternoon',
            'Brightcrown','Laughter and Cheer','Misty Garden','Love Poem','Sweet Cider Kiss','Dawning Dew','Gray Valley Sunset','Snow-Covered Kiss']

drink_prices = ['6.50','6.50','6.50','6.50','7.50','7.50','7.50','7.50','8.00','8.00','8.00','8.00','9.00','9.00']

num_drinks = 14

for count in range (num_drinks):
    print(count, drink_names[count], drink_prices[count]) #prints the drinks names and the drink price together in menu format