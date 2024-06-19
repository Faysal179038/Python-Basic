# copyfile() =  copies contents of a file
# copy()     =  copyfile() + permission mode + destination can be a directory
# copy2()    =  copy() + copies metedata (file's creation and modification times)

import shutil

shutil.copyfile(r"D:\learning\python\test.txt", r"D:\learning\python\test_copy.txt")
# shutil.copy(r"D:\learning\python\test.txt", r"D:\learning\python\test_copy.txt")
# shutil.copy2(r"D:\learning\python\test.txt", r"D:\learning\python\test_copy.txt")
