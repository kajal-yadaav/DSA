class Computer:
    def writecode(self,text):
        print("written code for",text)
    def execute(self):
        print("code executed")

class student:
    def dolabassignment(self,computer,assignment):
        #self.computers=computer
        computer.writecode(assignment)
        computer.execute()

s1=student()
c1=Computer()
s1.dolabassignment(c1,"sorting")
