x={'a':1,'b':2}
y={'b':3,'c':5}
m={**x,**y}
print(m)
n=dict(x,**y)
print(n)