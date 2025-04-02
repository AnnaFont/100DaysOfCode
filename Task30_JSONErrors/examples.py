import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Loop through rows of the data frame and save it in the dictionary
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
redo_question = True

while redo_question:
    user_in = input("Enter a word:").upper()

    try:
        list_code = [phonetic_dict[user_letter] for user_letter in user_in]
    except KeyError:
        print("Sorry, only letters in the alphabet")
        # Instead of using redo_question variable. It can be entered all the code in a function
        # and recall the function in here again
    else:
        redo_question = False
        print(list_code)








# To be used to something that might cause and exception
try:

    # To reach own exceptions
    # raise ValueError("This raise an error")
    pass
# Do this if there was an exception
except FileNotFoundError:
    pass
except KeyError as error_message:
    pass
# Do this if there were no exceptions
else:
    pass
# Do this always
finally:
    pass