# function = a block of code which is executed only when it is called.


def hello():
    print("Hello World!")
    print("This is a function")


hello()


# adding parameter
def hello(name):
    print(f"Hello {name}!")
    print("This is a function")


hello("killer")


# adding multiple parameters
my_first_name = "Killer"
my_last_name = "Elite"
my_age = 21


def hello(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")
    print("This is a function")


hello(my_first_name, my_last_name)


def hello(first_name, last_name, age):
    print(f"Hello {first_name} {last_name}!. you are {str(age)}")
    print("This is a function")


hello(my_first_name, my_last_name, my_age)
