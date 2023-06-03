shopping_cart = []
checkout = 0

while True:
    user_input = input("What would you like to buy? (press q to quit)\n")
    if user_input.lower() == "q":
        break
    else:
        try:
            price_input = float(input("What is the price?\n"))
            checkout += price_input
            shopping_cart.append(user_input)
        except:
            print("An exception occurred. Sorry for the inconvenience.")


print(f"Your shopping cart: {shopping_cart}, payment: {checkout}$")
