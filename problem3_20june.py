#180 rotation
n=int(input())
arr=[]
for i in range(n):
    l=list(map(int,input().split()))
    arr.append(l)

for i in range(n//2):
    for j in range(n):
        t=arr[i][j]
        arr[i][j]=arr[n-i-1][n-j-1]
        arr[n-i-1][n-j-1]=t

print(arr)