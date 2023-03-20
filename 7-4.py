pizza_toppings = []
active = True
while active:
    topping = input("Enter a topping for your pizza: ")
    pizza_toppings.append(topping)
    print("You have requested " + topping + ".")
    x = input("Would you like to add another topping (yes or no): ")
    if x == 'yes':
        continue
    else:
        active = False

print("Thank you for your order.")

print(pizza_toppings)
