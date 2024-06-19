# **kwargs =    parameter that will pack all arguments into a dictionary
#                useful so that a function can accept a varying number of keyword arguments


def hello(**kwargs):
    print(f"hello {kwargs['first']} {kwargs['last']}")
    print("hello", end=" ")
    for key, value in kwargs.items():
        print(value, end="")


hello(first="code", middle="forge", last="growth")
