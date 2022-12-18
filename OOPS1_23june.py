class Room:
    def __init__(self,rno):
        self.rno='A'+str(rno)

class Building:
    def __init__(self,room_count):
        self.rooms=[]
        for i in range(1,room_count+1):
            r=Room(i)
            print(r)

            self.rooms.append(r)
    def roominfo(self):
        for i in range(len(self.rooms)):
            print(self.rooms[i].rno)


b=Building(3)
print(len(b.rooms))
b.roominfo()
print(b)
del(b)

