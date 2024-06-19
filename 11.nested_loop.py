# nested loop = A loop within another loop (outer, inner)
#                          outer loop:
#                              inner loop:
#               "The inner loop" will finish all of its iterations before finishing one iteration of the "outer loop"

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
