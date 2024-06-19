text = "Have a nice day! See ya"

with open(
    r"D:\learning\python\test.txt", "a"
) as file:  # `w` will overwrite and `a` will append
    file.write(text)

with open(r"D:\learning\python\test.txt", "r") as file:
    print(file.read())
