# Define the menu of electronic gadgets
menu = {
    'Phone': 15000,
    'Laptop': 50000,
    'Headphone': 2000,
    'Charger': 800,
    'Powerbank': 1500,
}

# Greet
print("Welcome to PYTHON Electronic Gadgets Store")
print("Phone: Rs15000\nLaptop: Rs50000\nHeadphone: Rs2000\nCharger: Rs800\nPowerbank: Rs1500")

# Initialize the total order amount
order_total = 0

# Ask for the first order
item_1 = input("What would you like to order? ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Sorry, the ordered item {item_1} is not available yet!")

# Ask if the user wants to add another item
another_order = input("Do you want to add another item? (Yes/No) ")
if another_order.lower() == "yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order.")
    else:
        print(f"Sorry, the ordered item {item_2} is not available yet!")

# Display the total cost
print(f"The total cost of your order is Rs{order_total}")


