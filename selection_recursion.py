#recursive selection sort
#T(n) = n + T(n-1)
def selection(A,start,n):
    if start>=n-1:
        return
    minpos=start
    for i in range(start+1,n):
        if A[i]<A[minpos]:
            minpos=i
    A[start],A[minpos]=A[minpos],A[start]
    selection(A,start+1,n)
l=list(map(int,input().split()))
selection(l,0,len(l))
print(l)  
