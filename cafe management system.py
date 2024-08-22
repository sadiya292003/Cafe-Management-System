# Define the menu of the restaurant
menu = {
    'Pizza': 90,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
}

# Greet
print("Welcome to Savali Restaurant")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0

# First order
item_1 = input("Enter the name of the item you want to order: ").strip().title()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Ordered item {item_1} is not available yet!")

# Option to add more items
another_order = input("Do you want to add another item? (Yes/No): ").strip().title()
if another_order == "Yes":
    item_2 = input("Enter the name of the second item: ").strip().title()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order.")
    else:
        print(f"Ordered item {item_2} is not available!")

# Print the total amount
print(f"The total amount of items to pay is Rs{order_total}.") 