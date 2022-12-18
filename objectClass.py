class Employee:
    def __init__(self,fn,ln,id,des):
        self.__fname=fn
        self.__lname=ln
        self.__empID=id
        self.__designation=des
    def getname(self):
        return self.__fname+" "+self.__lname
    def getemail(self):
        return self.__fname+"."+self.__lname+'@psit.in'
    def getdesignation(self):
        return self.__designation
    def getempid(self):
        return self.__empID
emp1=Employee("KAJAL","YADAV",28825,"Student")
emp2=Employee("PALAK","GUPTA",28402,"Teacher")
emp3=Employee("ASTHA","BHARDWAJ",27796,"Student")
print(emp2.getemail())
print(emp1.getdesignation())
print(emp3.getempid())
print(emp2.getname())
