# List comprehension
# new_list = [new_item for item in list if test]
# Example:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = [n + 1 for n in numbers if n/2 == 0]
# For dictionaries
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Loop through rows of the data frame and save it in the dictionary
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
user_in = input("Enter a word:").upper()
list_code = [phonetic_dict[user_letter] for user_letter in user_in]
print(list_code)


