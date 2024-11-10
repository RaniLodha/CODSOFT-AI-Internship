# Product catalog with prices
product_catalog = {
    "apple": 1.5,
    "banana": 0.5,
    "orange": 0.75,
    "milk": 2.0,
    "bread": 1.25
}
# Shopping cart to store items and their quantities
cart = {}
# Function to show available items
def show_available_items():
    available_items = ", ".join(product_catalog.keys())  # Get the names of all items in the catalog
    return f"Available items to add to your cart: {available_items}"
# Function to add an item to the cart
def add_to_cart(item):
    if item in product_catalog:
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1
        return f"Added {item}. You now have {cart[item]} in your cart."
    else:
        return f"Sorry, {item} is not available in the store."
# Function to remove an item from the cart
def remove_from_cart(item):
    if item in cart:
        if cart[item] > 1:
            cart[item] -= 1
            return f"Removed one {item}. You now have {cart[item]} in your cart."
        elif cart[item] == 1:
            del cart[item]
            return f"Removed {item} from your cart."
    else:
        return f"{item} is not in your cart."
# Function to calculate the total cost
def calculate_total():
    total = sum(product_catalog[item] * quantity for item, quantity in cart.items())
    return f"Your total is ${total:.2f}"
# Function to handle chatbot responses
def chatbot_response(user_input):
    user_input = user_input.lower().split()  # Split input for easier command handling
    if "show" in user_input and "items" in user_input:
        return show_available_items()

    if "add" in user_input:
        item = user_input[-1]  # Assume the last word is the item name
        return add_to_cart(item)

    elif "remove" in user_input:
        item = user_input[-1]
        return remove_from_cart(item)
    elif "total" in user_input:
        return calculate_total()

    elif "show" in user_input and "cart" in user_input:
        if cart:
            return f"Your cart contains: {', '.join([f'{item}({qty})' for item, qty in cart.items()])}"
        else:
            return "Your cart is empty."
    else:
        return "I didn't understand that. You can 'add' or 'remove' items, or ask for the 'total'."
# Main chat loop
print("Welcome to the Shopping Cart Bot! Type 'exit' to end the conversation.")
while True:
    user_input = input("you: ")
    if user_input.lower() == "exit":
        print("Aston Bot: Goodbye Rani! Thank you for shopping.")
        break
    response = chatbot_response(user_input)
    print("Aston Bot:", response)
