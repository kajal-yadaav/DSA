def prime(n):
    c=0
    for j in range(1,n+1):
        if n%j==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
n=int(input())
i=0
t=1
while i!=n:
    a=prime(t)
    if a==1:
        print(t,end=" ")
        i+=1
    t+=1
    
