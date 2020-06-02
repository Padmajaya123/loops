d = {0:10, 1:20}
d2={7:30, 4:40}
d3={9:50,6:60}
print(d)
d.update({2:30})
d.update({5:77})
print(d)
d4={}
for i in (d,d2,d3): d4.update(i)
print(d4)