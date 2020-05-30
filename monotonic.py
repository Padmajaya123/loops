def Monotonic(a):

 return (all(a[i] <= a[i + 1] for i in range(len(a) - 1)) or
        all(a[i] >= a[i + 1] for i in range(len(a) - 1)))

a = [10,9,7,6, 5, 4, 4,1]
print(Monotonic(a))