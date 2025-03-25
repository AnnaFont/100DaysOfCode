# Function in charge to print the resources in the machine
def print_report(machine_resources):
    print("The current machine resources are as follows:")
    for resource in machine_resources:
        units = "ml"
        if resource == "coffee":
            units = "mg"
        elif resource == "money":
            units = "$"
        print(f" - {resource}: {round(machine_resources[resource],2)} {units}")


# Function in charge to check the resources in the machine
def check_resources(machine_resources,coffee_type,coffee_user):
    resource_ok = True
    # Compare each resource
    for resource in coffee_type[coffee_user]:
        if coffee_type[coffee_user][resource] > machine_resources[resource]:
            if not resource == "money":
                print(f"Sorry there is not enough {resource} to make your coffee.")
                resource_ok = False
    return resource_ok


# Function to check if there is enough money
def process_money(machine_resources,coffee_user,coffee_type):
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
    return enough_money, machine_resources


# Function in charge of updating the database after the user had the coffee
def reduce_resources(machine_resources,coffee_type,coffee_user):
    for resource in coffee_type[coffee_user]:
        if not resource == "money":
            machine_resources[resource] = machine_resources[resource] - coffee_type[coffee_user][resource]
    return machine_resources
