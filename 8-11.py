magicians = ['merlin', 'sigfried', 'david copperfield', 'houdini']
new_magicians = []


def make_great(magicians):
    for magician in magicians:
        new_magicians.append(magician + " the Great")


def show_magicians(magicians):
    """Print a list of the magicians performing."""
    print("\n")
    for magician in magicians:
        print(magician.title())


make_great(magicians[:])
show_magicians(magicians)
show_magicians(new_magicians)
