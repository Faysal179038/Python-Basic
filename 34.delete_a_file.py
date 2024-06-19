import os
import shutil

path = r"D:\learning\python\deleted_file.py"

try:
    os.remove(path)
except FileNotFoundError:
    print("That file was not found :(")

path = r"D:\learning\python\deleted_file.pt"

try:
    os.remove(path)
except FileNotFoundError:
    print("That file was not found :(")


path = r"D:\learning\python\deleted_file"

try:
    # os.remove(path)
    od.rmdir(path)  # `rmtre` for delete folder with file
except FileNotFoundError:
    print("That file was not found :(")
except PermissionError:
    print("You don't have permission to delete that file :(")
except OSError:
    print("You cannot delete that using that function")
else:
    print("The file has been deleted")
