class ClassA:
    def __init__(self):
        self.a=10
    def method(self):
        print(self.newb.b)

class ClassB:
    def __init__(self,obja):
        self.b=20
        self.obja=obja

    def method(self):
        print(self.obja.a)

obja=ClassA()
objb=ClassB(obja)
obja.newb=objb
obja.method()
