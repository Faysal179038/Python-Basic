# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Faysal", 21, "male")

print(student.count("Faysal"))
print(student.index("male"))

for x in student:
    print(x)

if "Faysal" in student:
    print("Faysal is here!")
