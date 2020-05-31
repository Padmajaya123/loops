def compoundinterest(p,r,t):
    C=p*(pow((1+r/100),t))
    print("Compound Interest=",C)

compoundinterest(10000, 10, 8)