import os

source = r"D:\learning\python\test.txt"
destination = r"D:\learning\python\test_move.txt"

try:
    if os.path.exists(destination):
        print(f"That {destination} already exists")
    else:
        os.replace(source, destination)
        print(f"{source} was moved")
except FileNotFoundError:
    print(f"That {source} was not found :(")


source = r"D:\learning\python\folder"
destination = r"D:\learning\python\New folder\folder"

try:
    if os.path.exists(destination):
        print(f"That {destination} already exists")
    else:
        os.replace(source, destination)
        print(f"{source} was moved")
except FileNotFoundError:
    print(f"That {source} was not found :(")
