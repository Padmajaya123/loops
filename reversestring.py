def reverse(str):
    r=''
    i=len(str)
    while i>0:
        r+=str[i-1]
        i=i-1
    return r
print(reverse('1234abcd'))
print(reverse('malayam'))