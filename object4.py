class study:
    a="maths"
    def __init__(self,name):
        self.name=name
    def marks(self,m):
        self.m=m
    def get(self):
        return self.m
r=study("computer")
r.marks(80)
print(r.get())