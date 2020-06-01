l1 = [1, 2, 3, 4, 5, 6,9,10]
l2 = [4, 5, 6, 7, 8,13]
print("Missing values in 2nd list:",(set(l1).difference(l2)))
print("Additional values in 2nd list:",(set(l2).difference(l1)))
print("Missing values in 1st list:",(set(l2).difference(l1)))
print("Additional values in 1st list:",(set(l1).difference(l2)))