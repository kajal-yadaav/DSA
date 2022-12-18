#find all common elements present in each row of a matrix
m=int(input())
n=int(input())
l=[]
for i in range(m):
    j=list(map(int,input().split()))
    l.append(j)
p=0
f=0
while p<n:
    f=0
    for i in range(m):
        #print(l[0][p])
        #print(l[i])
        if l[0][p] not in l[i]:
            f=1
            break
    if f==0:
        print(l[0][p],end=" ")
    p+=1
