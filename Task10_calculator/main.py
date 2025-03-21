# Calculator

def sum_func(a, b):
    return int(a)+int(b)


def subs_func(a, b):
    return int(a)-int(b)


def mult_func(a, b):
    return int(a)*int(b)


def div_func(a, b):
    if b != 0:
        return int(a)/int(b)
    else:
        return "inf"


operators = {
    "+": sum_func,
    "-": subs_func,
    "*": mult_func,
    "/": div_func,
}

print("Welcome to the python calculator")
num1 = input("Which is the first number?")
while True:
    operator = input("Which operation you want to do (+,-,*,/)?")
    num2 = input("Which is the next number?")
    result = operators[operator](num1, num2)
    print(f"{num1} {operator} {num2} = {result}")
    choice_user = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation:")
    if choice_user.lower() == "y":
        num1 = result
    else:
        print("\n"*20)
        num1 = input("Which is the first number?")
