# variabe = a container for a value. Behaves as the value that it contains

first_name = "Killer"  # string
last_name = "Elite"
full_name = first_name + " " + last_name
print("Hello ", full_name)  # prints: Faysal

age = 21  # int
age += 1
print(type(age))
print("youre age is: " + str(age))

print(f"Hello {first_name} {last_name}, you are {age} years old")  # prints: Faysal 21

height = 250.5  # float
print(type(height))
print("Your height is: " + str(height))

human = True  # boolean
print(human)
print(type(human))


print(
    f"Hello {first_name} {last_name}, you are {age} years old and your height is {height} cm and you are a {human} human"
)  # prints: Faysal 21 250.5 true


########################################################################################################################################
full_name, age, height, human = first_name + " " + last_name, 21, 250.0, True

print(
    f"Hello {full_name}, you are {age} years old and your height is {height} cm and you are a {human} human"
)  # prints: Faysal 21 250.5 true
