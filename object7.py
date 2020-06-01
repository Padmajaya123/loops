class study:
    sub="maths"
class big(study):
    pass
class higher(study):
    sub="computer"
r=big()
print(r.sub)
r1=higher()
print(r1.sub)