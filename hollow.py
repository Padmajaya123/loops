rows = int(input("Enter the total Number of Rows  :"))
columns = int(input("Enter the total Number of Columns  :"))
print("Hollow Box Pattern of Numbers")
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if (i == 1 or i == rows or j == 1 or j == columns):
            print('1', end='  ')
        else:
            print(' ', end='  ')
    print()