pizzas = ['sausage', 'pepperoni', 'fresh tomato']
friends_pizzas = pizzas[:]
pizzas.append('ham')
friends_pizzas.append('anchovie')

print("My favorite pizzas are:")
for x in pizzas:
    print(x)
print("\nMy friends favorite pizzas are:")
for x in friends_pizzas:
    print(x)
