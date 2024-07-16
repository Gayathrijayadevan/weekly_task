menu = {
    "1": {"name": "Pizza", "price": 8.99},
    "2": {"name": "Burger", "price": 5.99},
    "3": {"name": "Pasta", "price": 7.99},
    "4": {"name": "Salad", "price": 4.99}
}

def display_menu():
    print("\nMenu:")
    for item_id, item in menu.items():
        print(f"{item_id}. {item['name']} - ${item['price']}")

def get_item(item_id):
    return menu.get(item_id)

def admin_add(name,price):
    name = input("Enter the name of the new item: ")
    price = float(input("Enter the price of the new item: "))
    item_id = str(len(menu) + 1)  
    menu[item_id] = {"name": name, "price": price}
    print(f"Item '{name}' added to the menu.")

def  admin_delete():
    item_id = input("Enter the ID of the item to remove: ")
    if item_id in menu:
        del menu[item_id]
        print(f"Item with ID '{item_id}' removed from the menu.")
    else:
        print(f"Item with ID '{item_id}' not found in the menu.")