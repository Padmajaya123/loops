def test(s):
    u=0
    l=0
    for c in s:
        if c.isupper():
           u=u+1
        elif c.islower():
           l=l+1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", u)
    print ("No. of Lower case Characters : ", l)
test('The quick Brown Fox')