n1,n2,n3=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
c=[int(x) for x in input().split()]
list=[]
for i in a:
    if i in b and i in c:
        if i not in list:
            list.append(i)

print(list)
