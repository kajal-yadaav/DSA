class Stu:
    def __init__(self,name,id=5):
        self.name=name
        self.id=id
        print(self.id)

std=Stu("Simon",1)
std.id=2
print(std.id)