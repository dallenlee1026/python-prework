dave = {'first name': 'david', 'last name': 'lee', 'age': 61, 'city': 'alsip'}
andy = {'first name': 'andy', 'last name': 'richter',
        'age': 49, 'city': 'chicago'}
will = {'first name': 'will', 'last name': 'konrath',
        'age': 45, 'city': 'tinley park'}

people = [dave, andy, will]

for user in people:
    print("Name: " + user['first name'].title(), end=(" "))
    print(user['last name'].title())
    print("Age: " + str(user['age']))
    print("City: " + user['city'].title() + "\n")
