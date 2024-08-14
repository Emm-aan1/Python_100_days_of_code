class CoffeeMachine:
    def __init__(self, resources, menu):
        self.resources = resources
        self.menu = menu

    def report(self):
        """Prints a report of the coffee machine's resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.resources['money']:.2f}")

    def is_resource_sufficient(self, drink_name):
        """Checks if the coffee machine has enough resources to make a drink."""
        drink = self.menu[drink_name]
        for item in drink["ingredients"]:
            if self.resources[item] < drink["ingredients"][item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Processes the payment for the coffee."""
        payment = float(input("Insert money: $"))
        return payment

    def check_transaction(self, payment, drink_cost):
        """Checks if the inserted money is sufficient for the drink."""
        if payment >= drink_cost:
            change = round(payment - drink_cost, 2)
            print(f"Here is ${change} in change.")
            self.resources["money"] += drink_cost
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def make_coffee(self, drink_name):
        """Makes the specified coffee and updates resources."""
        drink = self.menu[drink_name]
        for item in drink["ingredients"]:
            self.resources[item] -= drink["ingredients"][item]
        print(f"Here is your {drink_name} ☕")

    def run(self):
        """Starts the coffee machine and handles user interactions."""
        while True:
            user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if user_choice == "off":
                break
            elif user_choice == "report":
                self.report()
            else:
                if user_choice in self.menu:
                    if self.is_resource_sufficient(user_choice):
                        payment = self.process_coins()
                        if self.check_transaction(payment, self.menu[user_choice]["cost"]):
                            self.make_coffee(user_choice)
                else:
                    print("Invalid choice. Please try again.")


if __name__ == "__main__":
    resources = {
        "water": 1000,
        "milk": 1000,
        "coffee": 250,
        "money": 0
    }

    MENU = {
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24
            },
            "cost": 1.5
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24
            },
            "cost": 1.2
        },
        "espresso": {
            "ingredients": {
                "water": 50,
                "milk": 0,
                "coffee": 18
            },
            "cost": 1.0
        }
    }

    coffee_machine = CoffeeMachine(resources, MENU)
    coffee_machine.run()
