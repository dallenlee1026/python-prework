rivers = {'nile': 'egypt', 'mississippi': 'america',
          'amazon': 'brazil', 'danube': 'france'}

# for river in rivers:
#    print("The " + river.title() + " runs through " + rivers[river].title() +
#          ".")
count = 1

for river in rivers:
    if count < len(rivers):
        print(river.title() + ",", end=" ")
        count += 1
    else:
        print("and " + river.title() + "\n")

count = 1

for country in rivers.values():
    if count < len(rivers):
        print(country.title() + ",", end=" ")
        count += 1
    else:
        print("and " + country.title())
