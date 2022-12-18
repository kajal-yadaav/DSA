#object of one class is pass to the function of another class
#when object/objects of one class is assigned to an instance variable of another clas then it is called has a relationship
class Player:
    def __init__(self,name):
        self.name=name
    def getplayer(self):
        return self.name
class team:
    def __init__(self):
        self.players=[]
    def addPlayer(self,player):
        self.players.append(player)

p1=Player('sachin') #create player
p2=Player("Kapil") #create another player
p3=Player("virat") #create another player

t=team()
t.addPlayer(p1)
t.addPlayer(p2)
t.addPlayer(p3)

print(t.players)
print(t.players[0].getplayer())
print(t.players[1].getplayer())
