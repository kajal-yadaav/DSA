def partition(A,lb,ub):
    start=lb
    end=ub
    pivot=A[0]
    while start<end:
        while A[start]<=pivot:
            start+=1
        while A[end]>pivot:
            end-=1
        t=A[start]
        A[start]=A[end]
        A[end]=t
    t=pivot
    pivot=A[end]
    A[end]=t
    return end
def quicksort(A,lb,ub):
    loc=partition(A,lb,ub)
    quicksort(A,lb,loc-1)
    quicksort(A,loc+1,ub)
n=int(input())
A=[]
for i in range(0,n):
    A.append(int(input()))
quicksort(A,0,n-1)
print(A)
