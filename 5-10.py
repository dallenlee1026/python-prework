current_users = ['joe2345', 'dallenlee1026',
                 'randy99', 'willmo', 'andys', 'stevelee']
new_users = ['raymondburr', 'dallenlee1026', 'Randy99', 'DaveW']

for name in new_users:
    if name.lower() in current_users:
        print(f'Username "{name}" is already taken. Please use another name.')
    else:
        print(f'Username "{name}" is accepted.')
