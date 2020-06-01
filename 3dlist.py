import pprint
def D(a,b,c):
    list = [[['#' for col in range(a)] for col in range(b)] for row in range(c)]
    return list
c1=5
c2=3
r=2
pprint.pprint(D(c1,c2,r))