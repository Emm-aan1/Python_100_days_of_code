from art import logo
from operations import add, sub, div, mult

print(logo)


def perform_operation(num1, num2, operation):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return sub(num1, num2)
    elif operation == '*':
        return mult(num1, num2)
    elif operation == '/':
        return div(num1, num2)
    else:
        return None


def calculator():
    continue_calc = True
    num1 = int(input("What is your first number?: "))

    while continue_calc:
        valid_operation = False
        while not valid_operation:
            for ops in ['+', '-', '*', '/']:
                print(ops)
            operation = input("Pick an operation: ")
            if operation in ['+', '-', '*', '/']:
                valid_operation = True
            else:
                print("Invalid operation: pick +, -, *, or /")

        num2 = int(input("What is your second number?: "))
        result = perform_operation(num1, num2, operation)
        print(f"{num1} {operation} {num2} = {result}")

        while True:
            print(f"Press 1 to continue with {result}")
            print("Press 2 to start over")
            print("Press 3 to exit")
            choice = input("Choose an option: ")
            if choice == '1':
                num1 = result
                break
            elif choice == '2':
                calculator()
                break
            elif choice == '3':
                continue_calc = False
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")


calculator()
