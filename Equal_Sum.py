n=int(input())
l=list(map(int,input().split()))
l.sort()
a=0
b=n-1
Sum=l[a]+l[b]
f=0
while a<b:
    if l[a]+l[b]!=Sum:
        f=1
        break
    a+=1
    b-=1
if f==1:
    print("FALSE")
else:
    print("TRUE")
