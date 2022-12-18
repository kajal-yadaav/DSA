l=list(map(int,input().split()))
n=len(l)
a=0
b=n-1
c=0
while a<=b:
    if l[a]!=l[b]:
        if l[a]<l[b]:
            l[a]+=l[a+1]
            l.remove(l[a+1])
            a+=1
        elif l[a]>l[b]:
            l[b]+=l[b-1]
            l.remove(l[b-1])
            b-=1
        c+=1
    a+=1
    b-=1
print(*l)
print(c)

