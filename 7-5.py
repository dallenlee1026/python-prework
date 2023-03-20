total_price = 0
active = True

while active:
    age = int(input("Please enter your age: "))
    if age < 3:
        print("Persons under 3 are Free.")
        total_price += 0
    elif age <= 12:
        print("The price is $10 for this guest.")
        total_price += 10
    else:
        print("The price is $15 for this guest.")
        total_price += 15

    x = input("Are there other guests in your party (Y/N) ")
    if x.title() == 'Y':
        continue
    else:
        print("The total price is $" + str(total_price) + ".")
        active = False
