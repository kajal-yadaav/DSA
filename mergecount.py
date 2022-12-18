A=list(map(int,input().split()))
l=len(A)
i=0
j=l-1
c=0
while i<=j:
    if A[i]!=A[j]:
        if A[i]<A[j]:
            A[i]+=A[i+1]
            A.remove(A[i+1])
            i+=1
        elif A[i]>A[j]:
            A[j]+=A[j-1]
            A.remove(A[j-1])
            j-=1
        c+=1
    i+=1
    j-=1
print(A)
print(c)
    