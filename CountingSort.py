def Counting_Sort(A,B,k):
    C=[0]*(k+1)
    for i in range(0,len(A)):
        C[A[i]]=C[A[i]]+1
    for i in range(1,k+1):
        C[i]=C[i]+C[i-1]
    print(C)
    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1]=A[j]
        C[A[j]]=C[A[j]]-1
    return B
A=list(map(int,input().split()))
B=[0]*len(A)
#B=A.copy()
k=max(A)
B=Counting_Sort(A,B,k)
print(*B)
