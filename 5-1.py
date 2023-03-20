alien = "grey"
score = 0

if alien == 'red':
    score += 25
    print("The alien is dead. You score " + str(score) + " points.")
elif alien == 'blue':
    score += 15
    print("The alien is dead. You score " + str(score) + " points.")
elif alien == 'yellow':
    score += 5
    print("The alien is dead. You score " + str(score) + " points.")
else:
    print("Nice try, but the alien lives on.")
