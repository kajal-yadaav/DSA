def Counting_Sort(A,k):
    C=[0]*(k+1)
    for i in range(0,len(A)):
        C[A[i]]=C[A[i]]+1
    print(C.index(2),end=" ")
    for i in range(1,len(C)):
        if C[i]==0:
            print(i)
A=list(map(int,input().split()))
#B=[0]*len(A)
#B=A.copy()
k=max(A)
Counting_Sort(A,k)
