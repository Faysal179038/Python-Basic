try:
    with open(r"D:\learning\python\test.txt") as file:
        print(file.read())
except FileExistsError:
    print("That file was not found :(")


print(file.closed)
