"""
numIn = int(input("Select a number: "))
if numIn % 2 == 0:
    print("Even")
elif numIn == 0:
    print("test")
else:
    print("Odd")
# Indentation: elif inside the if else (it is in the same start, no tab to add)

a = 2
b = a > 10 and a > 15  # or, not...
"""
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."  ` . "-._ /_______________|______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
# Welcome to treasure island
print("Welcome to Treasure Island")
LRin = input("You want to go left or right? (left/right)").lower()
if LRin == "left":
    # Syntax .lower() puts the input of the user in lowercase
    riverIn = input('You\'re at a crossroad.' 
                    'You need to cross he river. '
                    'You wait the boat or you swim? Type "boat" or "swim"').lower()
    if riverIn == "boat":
        doorIn = input("You find 3 doors. yellow/red/blue which one you choose?").lower()
        if doorIn == "yellow":
            print("Winner")
        else:
            print("Game over, you are a loser")
    else:
        print("The crocodile eats you. Game over, you are a loser")
else:
    print("You fall in a hole. Game over, you are a loser")
