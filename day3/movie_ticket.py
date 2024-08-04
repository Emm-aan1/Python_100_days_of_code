print("Welcome to the Max Rollercoaster ride. \nPlease purchase a ticket here 👇🏾")
user_height = int(input("How tall are you in 'CM'? "))

if user_height >= 120:
    print("You can ride the roller coaster")
    user_age = int(input("How old are you? "))
    ticket_price = 0
    answer = False

    while not answer:
        want_photo = input("Do you want a photo? Yes or No? ").strip().lower()
        if want_photo == 'yes':
            ticket_price += 3
            break
        elif want_photo == 'no':
            ticket_price = ticket_price
            answer = True

        else:
            print("Invalid: please enter 'yes' or 'no'.")
            # answer = True

    if user_age < 12:
        ticket_price += 3
        print(f"Please pay ${ticket_price}")
    elif 12 >= user_age <= 18:
        ticket_price += 5
        print(f"Please pay ${ticket_price}")
    elif user_age > 18:
        ticket_price += 7
        print(f"Please pay ${ticket_price}")

else:
    print("Sorry!, You are not tall enough to ride. 🥲")
