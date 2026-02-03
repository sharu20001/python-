while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = input("Enter amount: ")
        note = input("Enter note: ")

        with open("expenses.txt", "a") as file:
            file.write(amount + " - " + note + "\n")

        print(" Expense Saved!")

    elif choice == "2":
        try:
            with open("expenses.txt", "r") as file:
                data = file.read()
                print("\n Your Expenses:")
                print(data)
        except FileNotFoundError:
            print(" No expenses found yet")

    elif choice == "3":
        print(" Goodbye!")
        break

    else:
        print(" Invalid choice")
