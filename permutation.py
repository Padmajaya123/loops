from itertools import permutations
def Permutations(str):
    List = permutations(str)
    for perm in list(List):
        print(''.join(perm))
if __name__ == "__main__":
    s='REKHA'
    Permutations(s)