class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next=next_node


class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self,data):
        n=Node(data)
        if self.get_head()==None:
            self.__head=self.__tail=n
        else:
            self.__tail.set_next(n)
            self.__tail=n

    def display(self):
        temp=self.get_head()
        while temp!=None:
            print(temp.get_data())
            temp=temp.get_next()

    def find_node(self,data):
        temp=self.head
        while(temp is not None):
            if temp.get_data()==data:
                return temp
            temp=temp.get_next()
        return None

    def delete(self,data):
        node=self.find_node(data)
        if (node==self.__head):
            if node==self.__head==self.__tail:
                self.__tail=None
            self.__head=node.get_next()
        else:
            temp=self.__head
            while temp is not None:
                if temp.get_next()==node:
                    temp.set_next(node.get_next())
                    if node==self.__tail:
                        self.__tail=temp
                    node.set_next(None)
                    break
                temp=temp.get_next()
                else:
                    print(data,"is not present in list")

    def insert(self,data,data_before):
        new_node=Node(data)
        if data_before==None:
            new_node.set_next(self.__head)
            self.__head=new_node
            if new_node.get_next()==None:
                self.__tail=new_node
            else:
                node_before=self.find_node(data_before)
                if node_before is not None:
                    new_node.set_next(node_before.get_next())
                    node_before.set_next(new_node)
                    if new_node.get_next() is None:
                        self.__tail=new_node
                else:
                    print(data_before,"is not present in the Linked List")

    
##    def __str__(self):
##        temp=self._head
##        msg=[]
##        while(temp is not None):
##            msg.append(str(temp.get_data()))
##            temp=temp.get_next()
##        msg=" ".join(msg)
##        msg="LinkedList

list1=LinkedList() #LinkedList object list1 created
list1.add(20)
list1.add(30)
list1.add(40)
list1.display()

list1.delete(22)
list1.insert(55,33)
list1.display()


