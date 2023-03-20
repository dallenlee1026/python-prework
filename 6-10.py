users = {'Dave': ['61', '79'], 'Andy': ['45'], 'Will': [
    '40', '50'], 'Arno': ['35'], 'Steve': ['55', '75']}

for x, y in users.items():
    if len(y) > 1:
        print("\nName: " + x)
        print("Favorite Numbers:", end=(" "))
        for number in y:
            if number == y[-1]:
                print(number)
            else:
                print(number + ",", end=(" "))
    else:
        print("\nName: " + x)
        print("Favorite Number: " + y[0])
