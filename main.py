MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def show_report():
    """
    When a user enter the word 'report' they are given a report on remaining ingredients and amount of money in machine
    :return: Nothing, just prints a statement
    """
    report = f"Water: {resources['water']}ml" \
             f"\nMilk: {resources['milk']}ml" \
             f"\nCoffee: {resources['coffee']}g" \
             f"\nMoney: ${resources['money']} "
    print(report)


def check_resources(drink):
    """
    Check if there are enough resources to make the drink
    :param drink:
    :return: Returns the ingredient that is too low, or enough if there is enough of everything
    """
    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            return ingredient
    return "enough"


# Quarters = 0.25, Dimes = 0.10, Nickles = 0.05 and Pennies = 0.01
def process_coins():
    """
    Takes user money in coins
    :return: Returns the amount of those coins added up
    """
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    amount_entered = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return amount_entered


def manage_transaction(drink, money_entered):
    """
    Completes transaction between user and machine
    :param drink:
    :param money_entered:
    :return: Returns any change the user may have
    """
    drink_cost = MENU[drink]["cost"]
    if money_entered >= drink_cost:
        change = round(money_entered - drink_cost, 2)
        resources["money"] += drink_cost
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough. Money refunded.")
        return False


def make_coffee(drink):
    """
    Reduces the resources needed to make the drink
    :param drink:
    :return: Nothing, just a print statement
    """
    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here is your {drink} ☕️. Enjoy!")


def run_machine():
    """
    Main function for coffee machine
    :return: Nothing
    """
    machine_on = True
    while machine_on:
        chosen_drink = input("What would you like to drink? (espresso/latte/cappuccino): ").lower()
        if chosen_drink == "off":
            machine_on = False
        elif chosen_drink == "report":
            show_report()
        elif chosen_drink not in MENU:
            print("Don't recognize that drink ☹️.")
        else:
            resources_check = check_resources(chosen_drink)
            if resources_check != "enough":
                print(f"Sorry there is not enough {resources_check}.")
            else:
                amount_entered = process_coins()
                if manage_transaction(chosen_drink, amount_entered):
                    make_coffee(chosen_drink)


run_machine()
