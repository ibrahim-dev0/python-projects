balance = 0
history = []
account_created = False
name = ""


def show_menu(created):
    print("\nWelcome to Personal Bank")
    if not created:
        print("1. Create account")
        print("6. Exit")
    else:
        print("""
2. Deposit money
3. Withdraw money
4. Check balance
5. Transaction history
6. Exit
""")


def deposit(balance, history):
    amount = int(input("Deposit amount: "))
    balance += amount
    history.append({
        "type": "deposit",
        "amount": amount
    })
    return balance


def withdraw(balance, history):
    amount = int(input("Withdraw amount: "))
    if amount <= balance:
        balance -= amount
        history.append({
            "type": "withdraw",
            "amount": amount
        })
    else:
        print("Not enough balance")
    return balance


def show_history(history):
    if not history:
        print("No transactions yet")
        return

    for i, t in enumerate(history, 1):
        sign = "+" if t["type"] == "deposit" else "-"
        print(f"{i}. {t['type'].capitalize()} {sign}{t['amount']}")


while True:
    show_menu(account_created)
    choice = int(input("Choose: "))

    if not account_created:
        if choice == 1:
            name = input("Enter your name: ")
            account_created = True
            print(f"Account created. Welcome {name}!")
        elif choice == 6:
            print("Good luck")
            break
        else:
            print("Invalid choice")

    else:
        if choice == 2:
            balance = deposit(balance, history)

        elif choice == 3:
            balance = withdraw(balance, history)

        elif choice == 4:
            print(f"Current balance: {balance}")

        elif choice == 5:
            show_history(history)

        elif choice == 6:
            print("Good luck")
            break

        else:
            print("Invalid choice")
