t=int(input())
while t>0:
    a,b,c=map(int,input().split())
    p=abs(b-a)
    q=abs(c-b+1)
    if p>q:
        print(q)
    else:
        print(p)
    t-=1
