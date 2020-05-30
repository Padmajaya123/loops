s1=0
s2=0
for i in range(1,20):
    if i%2==0:
        print(i,"is a even number.")
        s1=s1+i
    else:
        print(i,"is a odd number.")
        s2=s2+i
print("sum of even=",s1)
print("sum of odd=",s2)
