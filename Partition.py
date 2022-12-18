l=list(map(int,input().split()))
f=1
length=len(l)
for i in range(0,length):
    S1=sum(l[0:i+1])
    S2=sum(l[i+1:length])
    if S1==S2:
        f=1
        break
if f==1:
    print(l[0:i+1],l[i+1:length],end=" ")
else:
    print("NOT POSSIBLE")
