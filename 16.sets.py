# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.add("fork")
# utensils.clear()
print("difference*******************")
print(utensils.difference(dishes))

print("commone************")
print(utensils.intersection(dishes))

print("update*******************")

utensils.update(dishes)
dishes.update(utensils)

dinner_table = utensils.union(dishes)


print("utensils*******************")
for x in utensils:
    print(x)

print("dishes*******************")
for x in dishes:
    print(x)

print("Dinner Table****************")
for x in dinner_table:
    print(x)
