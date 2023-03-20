favorite_places = {
    'dave': ['seattle', 'santa fe', 'san clemente'],
    'andy': ['chicago'],
    'will': ['milwaukee', 'indiana', 'ohio'],
}

for name, places in favorite_places.items():
    if len(places) > 1:
        print("\nMy name is " + name.title() + ", and my favorite places are:")
        for place in places:
            print("\t" + place.title())
    else:
        print("\nMy name is " + name.title() + ", and my favorite place is " +
              places[0].title() + ".")
