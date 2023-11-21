# We will be creating a coffee machine.
# Our coffee machine will have:
# 3 flavors: Cappuccino, Espresso, Latte:
# each flavor will have different quantities of recipes.
# Cappuccino: 250ml of water, 24g of coffee, 100ml of milk
# Latte: 200ml of water, 24g of coffee, 150ml of milk
# Espresso: 50ml of water, 18g of coffee
# Prices: 1.50(espresso), 2.50(latte), 3.00(cappuccino)
# Machine has: 300ml of water, 100g of coffee, 200ml of milk
# coin operated: penny(1 cent), nickel(5 cents), dime(10 cents), quarter(25 cents)
# coins in decimals: 0.01, 0.05, 0.10, 0.25
# Program Requirements:
# 1. Print report
# 2. Check resources sufficient
# 3. Process coins
# 4. Check transaction successful
# 5. Make coffee

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def is_resource_sufficient(order_ingredients):
    """This function checks if there are enough resources to make the order."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """This function processes the coins inserted by the user."""
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def check_transaction_successful(total, cost):
    """This function checks if the transaction is successful based on the total amount and the cost of the item."""
    if total >= cost:
        change = round(total - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """This function deducts the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if check_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


def print_report():
    """This function prints the current resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
