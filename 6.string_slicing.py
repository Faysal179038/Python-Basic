# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step], where start is inclusive and end is exclusive

name = "killer elite"
first_name = name[0:6]
# first_name = name[:6] #same
last_name = name[7:12]  # same
# last_name = name[7:]
funny_name = name[0:13:4]
# funny_name = name[::4] #same

print(first_name)  # prints: k
print(last_name)
print(funny_name)

reversed_name = name[::-1]
print(reversed_name)


website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)
print(website1[slice])
print(website2[slice])
