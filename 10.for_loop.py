import time

# for loops = execute a block of code a fixed number of times.
#                     You can iterate over a range, string, sequence, etc.

# ---------------- EXAMPLE 1 ----------------

for x in range(11):
    print(x)

# ---------------- EXAMPLE 2 ----------------
for i in range(50, 100 + 1, 2):
    print(i)

# ---------------- EXAMPLE 3 ----------------
for i in "faysal":
    print(i)

# ---------------- EXAMPLE 4 ----------------
for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")
