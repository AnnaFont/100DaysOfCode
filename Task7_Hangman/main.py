import random

stages_hangman = ('''
        
        |    
        |     
        |    
        |      
        |     
        |
      _ | ___

''', '''
        _______
        |    
        |     
        |    
        |      
        |     
        |
      _ | ___

''', '''
        _______
        | /   
        |  
        |    
        |      
        |     
        |
      _ | ___

''', '''
        _______
        | /    |
        |     
        |    
        |      
        |     
        |
      _ | ___

''', '''
        _______
        | /    |
        |     (_)
        |    
        |      
        |     
        |
      _ | ___

''', '''
        _______
        | /    |
        |     (_)
        |    \ | /
        |      
        |     
        |
      _ | ___

''', '''
        _______
        | /    |
        |     (_)
        |    \ | /
        |      |
        |     
        |
      _ | ___

''', '''
        _______
        | /    |
        |     (_)
        |    \ | /
        |      |
        |     / \ 
        |
      _ | ___

''')

print('''
88
88
88
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,  8b,dPPYba,
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8  88P'   `"8a
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88  88       88
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88  88       88
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8  88       88
                                    aa,    ,88
                                     "Y8bbdP"                                 

''')


# Hangman program
print("*******      Welcome to the hangman!      *******")
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango",
             "nectarine", "orange", "pear", "pineapple", "quince", "raspberry", "strawberry", "tomato", "ugli",
             "vanilla", "watermelon", "apricot", "blackberry", "blueberry", "cantaloupe", "coconut", "currant",
             "dragonfruit", "elderflower", "feijoa", "gooseberry", "jackfruit", "lychee", "melon", "mulberry", "papaya",
             "passionfruit", "peach", "plum", "pomegranate", "soursop", "tangerine", "tomatillo", "yuzu", "acai",
             "arava", "longan", "mandarin", "starfruit", "zucchini", "avocado", "pistachio", "cashew", "almond",
             "walnut", "hazelnut", "pecan", "macadamia", "brazil nut", "pine nut", "cucumber", "carrot", "celery",
             "spinach", "kale", "lettuce", "arugula", "beetroot", "chard", "broccoli", "cauliflower", "radish", "onion",
             "garlic", "shallot", "ginger", "turmeric", "bell pepper", "chili", "sweet potato", "potato", "yam",
             "eggplant", "zucchini", "artichoke", "asparagus", "brussels sprout", "turnip", "parsnip", "sweetcorn",
             "cabbage", "okra", "pumpkin", "squash", "snow pea", "edamame", "green bean", "lima bean", "soybean",
             "lentil", "chickpea", "black bean", "kidney bean", "pinto bean", "navy bean", "mung bean", "split pea",
             "aduki bean", "fava bean", "bean sprout", "tofu", "tempeh", "seitan", "rice", "quinoa", "barley", "bulgur",
             "farro", "oats", "wheat", "spelt", "buckwheat", "millet", "amaranth", "couscous", "pasta", "noodle",
             "ramen", "udon", "soba", "lasagna", "tortilla", "pita", "naan", "croissant", "baguette", "ciab"]

# Select a random word from the list
chosen_word = word_list[random.randint(0, 199)]
# it could be used also random.choice(word_list)
word_guess = ""
for letter in chosen_word:
    word_guess = word_guess + "_"
print(word_guess)
word_is_guessed = False
errors_made = 0
while not word_is_guessed and errors_made < 8:
    # Guess a letter from the word
    guess = input("Guess a letter: ").lower()

    letter_guessed = False
    # Check if guess is in the chosen_word by position
    for i in range(0, len(chosen_word)):
        # Simply can be used for letter in chosen_word and if guess == letter
        if guess == chosen_word[i]:
            # To replace a character in a string
            word_guess = word_guess[:i] + guess + word_guess[i + 1:]
            letter_guessed = True

    # The letter is not there
    if not letter_guessed:
        print("Wrong Letter")
        print(stages_hangman[errors_made])
        errors_made += 1

    if "_" not in word_guess:
        word_is_guessed = True

    print(word_guess)


if errors_made == 8:
    print("\n*********   LOOOOOOOOSEEEEER    *********")
    print("The world was", chosen_word)
else:
    print("\n*********   WIIIIIIINEEEEEER    *********")


