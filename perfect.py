def perfect(n):
    s=0
    for x in range(1, n):
        if n % x == 0:
            s=s+x
    return s==n
print(perfect(6))