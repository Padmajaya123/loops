def cube(n):
    s=0
    for i in range(1,n+1):
        s=s+(i*i*i)
    print("cube of first",n,"numbers are=",s)
cube(15)