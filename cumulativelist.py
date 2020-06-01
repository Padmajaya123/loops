def Cumulative(lists):
    c=[]
    length=len(lists)
    c=[sum(lists[0:x:1]) for x in range(0, length + 1)]
    return c[1:]

lists = [10, 20, 30, 40, 50,60,70]
print(Cumulative(lists))