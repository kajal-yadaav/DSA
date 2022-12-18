class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self._elements=[None]*self._max_size
        self.__top=-1

    def get_max_size(self):
       return self.__max_size


    def is_full(self):
       if(self.__top==self.__max_size-1):
           return True
       return False
    def is_empty(self):
      if(self.__top==-1):
          return True
      return False

    def push(self,data):
      if(self.is_full()):
          print("The stack is full!!")
      else:
          self.__top+=1
          self._elements[self._top]=data

    def pop(self):
     if(self.is_empty()):
         print("The stack is empty")
     else:
         index=self.top
         while(index>=0):
             print (self.__elements[index])
             index-=1
    def display (self):
        if(self.is_empty()):
            print("the stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1
                
        
    def str(self):
        msg=[]
        index=self.__top()
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=''.join(msg)
        msg="stack data (top to bottom):"+ msg


#new
def find_average(num_list):
        l=[]
        for i in range(num_list.get_max_size()):
            x=num_list.pop()
            if x==None:
                break
            l.append(x)
        av=sum(l)/len(l)
        print(av)
        for i in range(len(l)-1,-1,-1):
            num_list.push(l[i])

num_list=Stack(7)
num_list=Stack(78)
num_list=Stack(65)
num_list=Stack(92)
num_list=Stack(46)
num_list=Stack(89)
num_list=Stack(71)
num_list.display()
find_average(num_list)
num_list.display()
    
