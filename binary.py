def binary_search(l, num_find):
    start = 0
    end = len(l) - 1
    mid = (start + end) // 2
    found = False
    position = -1

    while start <= end:
        if l[mid] == num_find:
            found = True
            position = mid
            break

        if num_find > l[mid]:
            start = mid + 1
            mid = (start + end) // 2
        else:
            end = mid - 1
            mid = (start + end) // 2

    return (found, position)
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num = 7
found = binary_search(l, num)
if found[0]:
    print('Number found at position', (found[1] + 1))
else:
    print('Number not found=',num)