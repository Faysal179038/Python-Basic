# dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {
    "USA": "Washington DC",
    "India": "New Dehli",
    "China": "Beijing",
    "UK": "London",
    "Russia": "Moscow",
    "Bangladesh": "Dhaka",
}

print(capitals)
print(capitals["Russia"])
print(capitals.get("france"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)

capitals.update({"France": "Paris"})

print(capitals)
capitals.update({"USA": "Las Vegas"})
capitals.pop("Russia")
capitals.clear()

for key, value in capitals.items():
    print(key, value)
