t=int(input())
while t>0:
    k,n=map(int,input().split())
    a=k//5-n//5
    if n%5==0:
        a+=1
    if k%5==0 and k>0:
        a-=1
    print(a)
    t-=1 
