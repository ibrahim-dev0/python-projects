products = [
    {"name": "apple", "price": 2, "quantity": 10},
    {"name": "milk", "price": 3, "quantity": 5},
    {"name": "bread", "price": 1, "quantity": 20}
]

sales = []


def show_menu():
    print("""
Welcome to Mini Shop CLI
1. Show products
2. Buy product
3. Show sales
4. Exit
""")


def show_products(products):
    for i, product in enumerate(products, 1):
        print(f'{i}. {product["name"]} - price: {product["price"]}$ - Qty: {product["quantity"]}')


def buy_product(products, sales):
    show_products(products)
    choice = int(input("Which product do you want to buy: "))
    quantity = int(input("How many: "))

    if products[choice - 1]["quantity"] >= quantity:
        products[choice - 1]["quantity"] -= quantity
        sales.append({
            "product": products[choice - 1]["name"],
            "quantity": quantity,
            "total": products[choice - 1]["price"] * quantity
        })
        print(f"You bought {quantity} {products[choice - 1]['name']}")
    else:
        print("Not enough quantity!")


def show_sales(sales):
    if not sales:
        print("No sales yet")
        return

    for i, sale in enumerate(sales, 1):
        print(f"{i}. {sale['quantity']} {sale['product']} - Total: ${sale['total']}")


while True:
    show_menu()
    choice = int(input("Choose an option: "))

    if choice == 1:
        show_products(products)
    elif choice == 2:
        buy_product(products, sales)
    elif choice == 3:
        show_sales(sales)
    elif choice == 4:
        print("Thanks for visiting the shop!")
        break
    else:
        print("Invalid choice!")
