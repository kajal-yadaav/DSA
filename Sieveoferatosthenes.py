import math
def sieveoferantothese(n):
    arr=[True]*(n+1)
    arr[0]=False
    arr[1]=False
    for i in range(2,int(math.sqrt(n))+1):
        for j in range(2*i,n+1,i):
            arr[j]=False

    return arr

n=int(input())
l=sieveoferantothese(n)
for i in range(len(l)):
    if l[i]==True:
        print(i)

#print(int(math.sqrt(n)))