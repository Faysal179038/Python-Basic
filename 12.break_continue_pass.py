# Loop Control Statements = change a loops execution from its normal sequence

# break =       used to terminate the loop ectirely
# continue=     skips to the next iteration of the loop
# continue=     skips to the next iteration of the loop

# break =       used to terminate the loop ectirely
while True:
    name = input("Enter your name: ")
    if name != "":
        break

# continue=     skips to the next iteration of the loop
phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
# continue=     skips to the next iteration of the loop

for letter in "Python":
    if letter == "h":
        pass
        print("This is pass block")
    print(" Current Letter :", letter)
