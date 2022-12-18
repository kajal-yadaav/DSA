t=int(input())
while t>0:
    n,m=map(int,input().split())
    listt=[]
    p=1
    for i in range(n):
        d=2
        l=[]
        for j in range(m):
            l.append(p*(j+1))
        listt.append(l)
        p+=d 
    for i in range(n):
        print(*listt[i])
    t-=1


