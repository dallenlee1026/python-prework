favorite_languages = {
    'dave': 'cobalt',
    'andy': 'c',
    'will': 'python',
    'steve': 'java',
    'jack': 'ruby',
    'tom': 'python',
}

polling = ['dave', 'andy', 'carl', 'will', 'henry', 'steve', 'jack', 'tom']

for name in polling:
    if name not in favorite_languages:
        print("Hello " + name.title() + ", please respond to the poll.")
    else:
        print("Thank you for responding, " + name.title() + ".")
