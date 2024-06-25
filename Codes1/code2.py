
class Pe:
    def __init__(self, name):
        self.name = name

    def fun1(self):
        print("Hello, ", self.name)


pvar: Pe = Pe("Hell")
pvar.fun1()
