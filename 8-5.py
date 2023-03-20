def describe_city(name, country='united states'):
    """Display a cities name and the country where it is located."""
    print("\n" + name.title() + " is located in " + country.title() + ".")


describe_city('chicago')
describe_city('cleveland')
describe_city('moscow', 'russia')
