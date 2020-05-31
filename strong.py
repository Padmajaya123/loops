a=int(input("enter a number="))
t=a
s=0
while a>0:
    d=a%10
    f=1
    for i in range(1,d+1):
        f=f*i
    s=s+f
    a=a//10
if s==t:
    print(t,"is a strong no.")
