class Animal():
    def talk(self):
        pass
class Cat(Animal):
    def talk(self):
        print("Meow")

class Dog(Animal):
    def talk(self):
        print("woof")

class AnimalTalkShow:
    def dias(self,guest):
        if isinstance(guest,Animal):
            guest.talk()
        else:
            print("not atlowed")

show=AnimalTalkShow()
c=Cat()
show.dias(c)
d=Dog()
show.dias(d)
