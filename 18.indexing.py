# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "killer Elite"

if name[0].islower():
    name = name.capitalize()

print(name)

first_name = name[:6].upper()
last_name = name[7:]

print(f"first name: {first_name}")
print(f"last name: {last_name}")
last_character = name[-1]
print(f"last character {last_character}")
