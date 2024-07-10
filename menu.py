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