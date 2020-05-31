str="hello world programming"
print("original string=",str)
n=int(input("enter the position to remove="))
s=""
for i in range(len(str)):
    if i!=(n-1):
        s=s+str[i]
print("new string=",s)