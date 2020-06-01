from itertools import permutations
def Permutations(str):
    List = permutations(str)
    for perm in list(List):
        print(''.join(perm))

s='REKHA'
Permutations(s)