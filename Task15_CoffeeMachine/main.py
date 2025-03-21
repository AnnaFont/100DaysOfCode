# Coffee Machine
machine_resources = {
    "water": 100,
    "milk": 200,
    "coffee": 300,
    "money": 0
}
coffee_type = {
    "espresso": {
        "water": 25,
        "milk": 0,
        "coffee": 50,
        "money": 1
    },
    "latte": {
        "water": 50,
        "milk": 50,
        "coffee": 50,
        "money": 2
    },
    "cappuccino": {
        "water": 100,
        "milk": 100,
        "coffee": 50,
        "money": 3
    }
}


# Function in charge to print the resources in the machine
def print_report():
    print("The current machine resources are as follows:")
    for resource in machine_resources:
        units = "ml"
        if resource == "coffee":
            units = "mg"
        elif resource == "money":
            units = "$"
        print(f" - {resource}: {round(machine_resources[resource],2)} {units}")


# Function in charge to check the resources in the machine
def check_resources():
    resource_ok = True
    # Compare each resource
    for resource in coffee_type[coffee_user]:
        if coffee_type[coffee_user][resource] > machine_resources[resource]:
            if not resource == "money":
                print(f"Sorry there is not enough {resource} to make your coffee.")
                resource_ok = False
    return resource_ok


# Function to check if there is enough money
def process_money():
    enough_money = True
    print(f"Your {coffee_user} costs ${coffee_type[coffee_user]['money']}")
    print("Insert the coins to continue")
    quarters_in = float(input("How many quarters?"))
    dimes_in = float(input("How many dimes?"))
    nickles_in = float(input("How many nickles?"))
    pennies_in = float(input("How many pennies?"))
    # Calculate money inserted
    total_amount = round(pennies_in * 0.01 + nickles_in*0.05 + dimes_in*0.1 + quarters_in*0.25, 2)
    print(f"You have inserted ${total_amount}")
    # Check if enough to pay the coffee
    difference_money = round(total_amount + machine_resources["money"] - coffee_type[coffee_user]["money"], 2)
    if difference_money > 0:
        print(f"Your change is ${difference_money}")
        machine_resources["money"] = 0
    elif difference_money < 0:
        print("There is not enough money, get your change")
        enough_money = False
    else:
        machine_resources["money"] = 0
    return enough_money


# Function in charge of updating the database after the user had the coffee
def reduce_resources():
    for resource in coffee_type[coffee_user]:
        if not resource == "money":
            machine_resources[resource] = machine_resources[resource] - coffee_type[coffee_user][resource]


########################################################################################


print("Welcome to the coffee machine ☕☕☕")
machine_on = True

while machine_on:
    # 1. Prompt what they like
    coffee_user = input("What would you like? (espresso/latte/cappuccino)\n")
    # 2. Check off
    if coffee_user == "off":
        machine_on = False
    elif coffee_user == "report":
        # 3. Print report (Water/Milk/Coffee/Money)
        print_report()
    else:
        # 4. Check resources
        if check_resources():
            # 5. Process coins and
            # 6. Transaction ok
            if process_money():
                # 7. Make coffee
                reduce_resources()
                print(f"Here is your {coffee_user}. Enjoy!")
