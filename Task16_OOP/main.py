# OOP - Object Oriented Programming
# Goal: Coffee Machine with OOP

from machine_database import MachineResources
from machine_database import CoffeType
# Coffee Machine

import ext_programs
########################################################################################

machine_resources = MachineResources()
coffee_type = CoffeType()
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
        ext_programs.print_report(machine_resources)
    else:
        # 4. Check resources
        if ext_programs.check_resources(machine_resources, coffee_type, coffee_user):
            # 5. Process coins and
            # 6. Transaction ok
            [enough_money, machine_resources] = ext_programs.process_money(machine_resources, coffee_user, coffee_type)
            if enough_money:
                # 7. Make coffee
                machine_resources = ext_programs.reduce_resources(machine_resources, coffee_type, coffee_user)
                print(f"Here is your {coffee_user}. Enjoy!")
