l=int(input("lower range: "))
u=int(input("upper range: "))
print("Armstrong numbers")
for i in range(l,u+1):
    s=0
    t=i
    while t>0:
        d=t%10
        s=s+d**3
        t=t/10
        if i==s:
            print(i)