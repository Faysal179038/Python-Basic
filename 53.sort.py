# sort() method   = used with lists
# sort() function = used with iterables

# -----------------------------------sort() method-----------------------------------------------
students1 = ["Squidward", "Sandy" "Patrick", "Spongebob", "Mr.Krabs"]  # list

students1.sort(reverse=True)

for i in students1:
    print(i)


print("---------------------------------------")

# -----------------------------------sort() function-----------------------------------------------
students2 = ("Squidward", "Sandy" "Patrick", "Spongebob", "Mr.Krabs")  # tuple

sorted_students = sorted(students2, reverse=True)

for i in students1:
    print(i)

print("---------------------------------------")

# ----------------------------------------------------------------------------------

students3 = [
    (
        ("Squidward", "F", 60),
        ("Sandy", "A", 33),
        ("Patrick", "D", 36),
        ("Spongebob", "B", 20),
        ("Mr.Krabs", "C", 78),
    )
]

grade = lambda grades: grades[1]
students3.sort(key=grade, reverse=True)  # sorts current list

for i in students3:
    print(i)

age = lambda ages: ages[1]
students3.sort(key=age, reverse=True)  # sorts current list
for i in students3:
    print(i)


print("---------------------------------------")

# ----------------------------------------------------------------------------------


students = (
    ("Squidward", "F", 60),
    ("Sandy", "A", 33),
    ("Patrick", "D", 36),
    ("Spongebob", "B", 20),
    ("Mr.Krabs", "C", 78),
)

grade = lambda grades: grades[1]
# students.sort(key=age)                                       # sorts current list
sorted_students = sorted(students, key=grade)  # sorts and creates a new list

for i in sorted_students:
    print(i)
