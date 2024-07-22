import utils

orders = []

def create_order(username, item, quantity):
    order_id = utils.generate_order_id()
    order = {
        "order_id": order_id,
        "username": username,
        "item": item,
        "quantity": quantity,
        "total_price": item['price'] * quantity
    }
    orders.append(order)

def view_orders(username):
    user_orders = [order for order in orders if order['username'] == username]
    if user_orders:
        print("\nYour Orders:")
        for order in user_orders:
            print(f"Order ID: {order['order_id']}, Item: {order['item']['name']}, Quantity: {order['quantity']}, Total Price: ${order['total_price']:.2f}")
    else:
        print("No orders found.")


def cancel_order(order_id, username):
    global orders
    order = next((order for order in orders if order['order_id'] == order_id and order['username'] == username), None)
    if order:
        orders = [order for order in orders if order['order_id'] != order_id]
        return True
    return False

def admin_view_order():
    for i in orders:
        print(i)



# def view_orders(username):
#     user_orders = [order for order in orders if order['username'] == username]
#     if user_orders:
#         print("\nYour Orders:")
#         for order in user_orders:
#             print(f"Order ID: {order['order_id']}, Item: {order['item']['name']}, Quantity: {order['quantity']}, Total Price: ${order['total_price']:.2f}")
#     else:
#         print("No orders found.")
