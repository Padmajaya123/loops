def vow(string,v):
    f=[each for each in string if each in v]
    print(len(f))
    print(f)

string="Hello World Programming"
v="AaEeIiOoUu"
vow(string,v);