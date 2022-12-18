class Employee:
    def __init__(self,first,last,sal):
        self.fname=first
        self.lname=last
        self.salary=sal
    def fullname(self):
        print(self.fname+" "+self.lname)

class Developer(Employee):
    def __init__(self,first,last,sal,prog_lang):
        super().__init__(first,last,sal)
        self.language=prog_lang
    def fullname(self):
        super().fullname()
        print(self.fname+" "+self.lname+" The Developers")
    def getlanguage(self):
        return self.language

#-------------------------------------------------------------

dev1=Developer("Mohit","Kumar",15000,"Python")
dev2=Developer("Mohit","Kumar",15000,"Python")
