n = int(input("No of terms in fibonacci? "))
n1 = 0
n2 = 1
c=2
if n<=0:
    print("enter a positive integer")
elif n== 1:
    print("Fibonacci sequence:")
    print(n1)
else:
    print("Fibonacci sequence:")
    print(n1, ",", n2,end=', ')
    while c<n:
        n3 = n1 + n2
        print(n3,end=' , ')
        n1 = n2
        n2 = n3
        c+= 1