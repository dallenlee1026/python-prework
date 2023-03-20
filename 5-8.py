users = []
name = 'will'
name = name.title()
users.append(name)

if users == []:
    print(f"Sorry {name}, we need to register all users!")
    print("The Admin has been notified.")
elif name in users:
    if name == 'Admin':
        print(f"Hello {name}, would you like a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")
else:
    print(f"We're sorry, {name}, you are not currently registered.")
