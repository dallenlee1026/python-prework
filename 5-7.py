favorite_fruits = ['apples', 'oranges', 'watermelon']
fruits = ['apples', 'oranges', 'bananas', 'watermelon', 'grapes', 'cherries']

for fruit in fruits:
    if fruit in favorite_fruits:
        print(f"I love {fruit}!")
    else:
        print(f"I don't care for {fruit}.")
