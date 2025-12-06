# Pizzeria Prototype w/ nested if-else

print("Welcome to Mansoor's Pizzeria!\n")

user_input = ""
while user_input != "Exit":
    print("Please order from the options below.\n")
    print("1. Cheese Pizza\n")
    print("2. Pepperoni Pizza\n")
    print("3. Supreme Pizza\n")
    print("Type 'Exit' to leave.\n")

    user_input = input("Enter the order number: ")

    if user_input == "1":
        print("Cheese Pizza coming right up!\n")

    elif user_input == "2":
        print("Pepperoni Pizza coming right up!\n")

    elif user_input == "3":
        print("Supreme Pizza coming right up!\n")

    elif user_input == "Exit":
        print("Goodbye! Thanks for visiting Mansoor's Pizzeria.\n")

    else:
        print("Invalid option, please try again.\n")
