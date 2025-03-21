# Randomization - import library
import random
import time
'''
# random.uniform
randomNum = random.randint(1, 2)
if randomNum == 1:
    print("Heads")
else:
    print("Tails")

# extending arrays
arrayExample = ["a", "b"]
arrayExample.extend("c")
print(arrayExample)

list_A = ["ab", "ad", "a_pick_me"]
list_B = ["bc", "bb"]
list_C = [list_A, list_B]
print(list_C)
print(list_C[0][2])
'''

print("Welcome to the Rock Paper Scissors game")
imgScissors =('''

   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.
''')
imgRock =('''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'      
''')
imgPaper = ('''
                     _.-._
                    | | | |_
                    | | | | |
                    | | | | |
                  _ |  '-._ |
                  \`\`-.'-._;
                   \    '   |
                    \  .`  /
                     |    |
''')

gameChoices = ["scissors", "rock", "paper"]
imgChoices = [imgScissors, imgRock, imgPaper]

choiceIn = int(input("Which one you pick? Type 0 for Scissors, 1 for Rock or 2 for Paper\n"))
# Also can be used random.choice(gameChoices)
choicePC = (random.randint(0, 2))
if 0 <= choiceIn <= 3:
    print("You picked... ", choiceIn, "-", gameChoices[choiceIn], "\n", imgChoices[choiceIn])
    time.sleep(1)
    print("Computer picked... ", gameChoices[choicePC], "\n", imgChoices[choicePC])
    time.sleep(1)

    if choicePC == choiceIn:
        print("Equal, noone wins")
    elif choicePC == 0 and choiceIn == 1 or choicePC == 1 and choiceIn == 2 or choicePC == 2 and choiceIn == 0:
        print("****  YOU ARE THE WINNER   ****")
        print('''
                 ___________
                '._==_==_=_.'
                .-\:      /-.
               | (|:.     |) |
                '-|:.     |-'
                  \::.    /
                   '::. .'
                     ) (
                   _.' '._
                  `"""""""`
        ''')
    else:
        print("Loooooooser :/ :/ :/")
else:
    print("You have selected a wrong number")
    
