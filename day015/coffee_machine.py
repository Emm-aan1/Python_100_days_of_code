from resources import resources, MENU


def report():
    """Prints a report of the coffee machine's resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


def is_resource_sufficient(drink):
    """Checks if the coffee machine has enough resources to make a drink."""
    for item in MENU[drink]["ingredients"]:
        if resources[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def process_coins():
    """Processes the payment for the coffee."""
    payment = float(input("Insert money: $"))
    return payment


def check_transaction(payment, drink_cost):
    """Checks if the inserted money is sufficient for the drink."""
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink):
    """Makes the specified coffee and updates resources."""
    resources["money"] += MENU[drink]["cost"]
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    print(f"Here is your {drink} ☕")


def run():
    """Starts the coffee machine and handles user interactions."""
    while True:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "off":
            break
        elif user_choice == "report":
            report()
        else:
            drink = MENU.get(user_choice)
            if drink:
                if is_resource_sufficient(user_choice):
                    payment = process_coins()
                    if check_transaction(payment, drink["cost"]):
                        make_coffee(user_choice)
                else:
                    print("Sorry, there is not enough resources.")
            else:
                print("Invalid choice. Please try again.")


run()
