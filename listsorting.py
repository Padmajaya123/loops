def Sorting(list):
    list2 = sorted(list,key=len)
    return list2

list = ["rohan", "samy", "swathy", "mohan",
       "meena", "reema", "chandrika"]
print(Sorting(list))