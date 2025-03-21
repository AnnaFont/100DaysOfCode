"""
# Loops
fruits = ["Apple", "Pear"]
for fruit in fruits:
    print(fruit)
student_scores = [32, 54, 87, 11, 69]
# Sum the whole array
totalScore = sum(student_scores)
maxScore = max(student_scores)
print("Total Score:", totalScore, "\nMaximum Score:", maxScore)
# Range function
sumGauss = 0
for gaussNum in range(1, 101):
    sumGauss += gaussNum
print(sumGauss)
"""

# Password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Hard Level - Order of characters randomised
arrayCum = []
# Pick random letters
for i in range(0, nr_letters):
    arrayCum.append(random.choice(letters))
# Pick random symbols
for i in range(0, nr_symbols):
    arrayCum.append(random.choice(symbols))
# Pick random numbers
for i in range(0, nr_numbers):
    arrayCum.append(random.choice(numbers))

# Change order
random.shuffle(arrayCum)

passGen = ""
for char in arrayCum:
    passGen += char
print("Password Shuffled: ", passGen)