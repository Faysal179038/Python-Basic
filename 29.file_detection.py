import os

path = r"D:\learning\python\test.txt"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That location is a file")
    elif os.path.isdir(path):
        print("That location is a directory")
    else:
        print("That location is not a file")
else:
    print("That location dosen't exists")
