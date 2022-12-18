#XORING COodechef
t=int(input())
while t>0:
    a,b,n=map(int,input().split())
    S=a^b
    if a!=b:
        if S<=n:
            print(abs(S-a))
        else:
            print(-1)
    else:
        print(0)
    t-=1