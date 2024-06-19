# *args =   parameter that will pack all arguments into a tuple
#           useful so that a function can accept a varying amount of arguments


def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3))

print(add(1, 2, 3))


print("stuff")


def add2(*stuff):
    sum = 0
    print(sum)
    stuff = list(stuff)
    print(stuff)
    stuff[0] = 0
    # print(stuff)
    for i in stuff:
        sum += i
    return sum


print(add2(4, 5, 7))
