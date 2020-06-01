def lists(list1):
    sublist=[[]]
    for i in range(len(list1) + 1):
        for j in range(i+1,len(list1) + 1):
            s=list1[i:j]
            sublist.append(s)

    return sublist
l=[1, 2, 3,4,5]
print(lists(l))