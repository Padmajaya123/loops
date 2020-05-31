def simpleinterest(p,t,r):
    print('The principal=',p)
    print('The time period=',t)
    print('The rate of interest=',r)
    s=(p*t*r)/100
    print('The Simple Interest=',s)
    return s
simpleinterest(12,4,5)