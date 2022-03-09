#!/usr/bin/env python3
''' Sahil Koul 
    If, elif & else conditionals'''

greeting = "Good Day !! You feel like eating"
print("Food Options are:1=Indian, 2=Italian, 3=Chinese, 4=Greek")
food = input("What would you like to eat?").lower() # Asks user to input fav food
    

if food == 'indian' or food == '1':
   greeting = f'{greeting} Indian, Calling Taj Mahel Resturant.'
elif food == 'italian' or food == '2':
    greeting = f'{greeting} Italian, Calling Olive Garden Resturant.'
elif food == 'chinese' or food == '3':
    greeting = f'{greeting} Chinese, Calling Yo China!  Resturant.'
elif food == 'greek' or food == '4':
    greeting = f'{greeting} Greek, Calling Classic Greek Resturant.'
else:
    greeting = "Option not in list"

print(greeting)





    
