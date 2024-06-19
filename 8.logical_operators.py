# logical operators = used on conditional statements

#              and = checks two or more conditions are True
#               or = checks if at least one condition is True
#              not = True if condition is False, and vice versa

sunny = True

print("The and,or operators")
temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("The temperature is good")
    print("go outside!")
elif temp < 0 or temp > 30:
    print("The temperature is bad today")
    print("stay home!")


print("The not operators")
temp = int(input("What is the temperature outside?: "))

if not (temp >= 0 and temp <= 30):
    print("The temperature is good")
    print("go outside!")
elif not (temp < 0 or temp > 30):
    print("The temperature is bad today")
    print("stay home!")
