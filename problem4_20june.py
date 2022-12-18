#print all combinations of phrase

list1=list(input().split())
list2=list(input().split())
list3=list(input().split())

for i in list1:
    for j in list2:
        for k in list3:
            print(i,j,k,end=" ")
            print()