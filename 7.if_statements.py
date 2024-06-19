# if statement =  a block of code that will execute if its condition is true

age = int(input("How old are you?: "))

if age == 100:
    print("You are a centenarian!")
elif age >= 18:
    print("You are an adult!")
    print("You can vote!")
    print("You can rent a car!")
elif age < 0:
    print("You have't been bron yet!")
else:
    print("You are not a child!")
