n=int(input("enter value of n="))
a=[]
s=0.0
for i in range(0,n):
    k=int(input("enter the value="))
    a.append(k)
s=sum(a)/n
print("Average of elements in list=",s)