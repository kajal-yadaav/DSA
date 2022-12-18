L=list(map(int,input().split()))
n=len(L)
i=0
j=n-1
while i<=j:
    if L[i]<0:
        i+=1
    elif L[j]>0:
        j-=1
    else:
        L[i],L[j]=L[j],L[i]
print(L)
