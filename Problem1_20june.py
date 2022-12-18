#find the output array from given inputed array
import math
m=int(input())
l=list(map(int,input().split()))
n=(1+int(math.sqrt(1+8*m))//2)
print(n)
B=[]
if n==1 or m==1:
    B.append(l[0])
elif n==2:
    B.append(l[0]-l[1])
else:
    B.append((l[0]+l[1]-l[n-1])//2)

for i in range(1,n):
    B.append(l[i]-B[0])

print(B)
