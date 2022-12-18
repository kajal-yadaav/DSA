list=[]
def pushh(x):
    list.append(x)
def popp():
    list.pop()
s=input()
for i in s:
    l=len(list)
    if i=='+':
        a=list[l-1]+list[l-2]
        pushh(a)
    elif i=='D':
        a=list[l-1]*2
        pushh(a)
    elif i=='C':
        popp()
    else:
        pushh(int(i))
print(sum(list))
