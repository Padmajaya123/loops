r=int(input("Input the number of rows "))
for i in range(1,r):
    for j in range(i,0,-1):
        print(j,end=' ')
    print("")