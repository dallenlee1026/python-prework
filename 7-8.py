sandwich_orders = ['pastrami', 'tuna', 'roast beef',
                   'pastrami', 'meatball', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    if sandwich == 'pastrami':
        print("Sorry, but we are all out of " + sandwich)
    else:
        print("The " + sandwich + " sandwich is ready.")
        finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been prepared:")
for sandwich in finished_sandwiches:
    print(sandwich + " sandwich")

print(sandwich_orders)
print(finished_sandwiches)
