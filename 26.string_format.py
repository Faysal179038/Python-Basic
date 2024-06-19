# str.format() =    optional method that gives users
#                   more control when displaying output

animal = "cow"
item = "moon"

# print(f"the {animal} jumped over the {item}")
print("the {} jumped over the {}".format(animal, item))
print("the {1} jumped over the {0}".format(animal, item))  # positional argument
print(
    "the {animal} jumped over the {item}".format(animal="cow", item="moon")
)  # keyword argument


text = "the {} jumped over the {}"
print(text.format(animal, item))  # positional argument


name = "code"

print("Hello my is {}".format(name))
print("Hello my is {:10}. Nice to meet you".format(name))
print("Hello my is {:<10}. Nice to meet you".format(name))  # LHS
print("Hello my is {:>10}. Nice to meet you".format(name))  # RHS
print("Hello my is {:^10}. Nice to meet you".format(name))  # Center


pi_number = 3.14159
print("The number pi is {:.2f}".format(pi_number))  # 2 decimal places

print("The number pi is {:.3f}".format(pi_number))  # 3 decimal places

number = 1000
print("The number is {:,}".format(number))  # 3 decimal places
print("The number is {:b}".format(number))  # 3 decimal places
print("The number is {:o}".format(number))  # 3 decimal places
print("The number is {:X}".format(number))  # 3 decimal places
