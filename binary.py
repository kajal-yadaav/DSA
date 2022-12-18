n=int(input())
list=[]
def enqueue(x):
    list.append(x)
def dequeue():
    print(list.pop(0),end=" ")
a='1'
print(a,end=" ")
for i in range(1,n):
    enqueue((a+'0'))
    enqueue((a+'1'))
    a=list[0]
    dequeue()
