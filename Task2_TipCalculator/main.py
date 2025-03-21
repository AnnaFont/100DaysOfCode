# Task 2 info
"""
# Subscripting - take one character of the string
print("Hello"[1])
print("Hello"[-4])

# Strings vs Number data type
print("12" + "34")
print(12 + 34)
print(int("12")+int("34"))
print(True)

# Check data type
print(type("hi"))
print(type(123))
print(type(123.123))
print(type(True))
# Float
print(8/3)
# Integer (no decimals - wiped out)
print(8//3)

# squared is a ** 2
# round decimals -> round(number, digits)

#Short sum
score += 1

# It can be use an f to mix types of data in a string
score = 1
height = 2.3
print(f"Your score is = {score}, your height is {height}")

"""

# Tip Calculator
print("Welcome to the tip calculator!")
billTotalIn = float(input("What was the total bill? $"))
tipIn = int(input("Which tip you want to give? 10, 12 or 15? "))
peopleIn = int(input("How many you were?\n"))
pricePP = round(billTotalIn * (1 + tipIn / 100) / peopleIn, 2)
print(f"Each person should pay:{pricePP}")
