num1=[]
num2=[]
num1=list(map(int,input().split()))
num2=[int(x) for x in input().split()]
l1=len(num1)
l2=len(num2)
for i in num1:
    a=num2.index(i)
    a1=num1.index(i)
    if a==l2-1:
        num1[a1]=-1
    elif num2[a+1]<i:
        num1[a1]=-1
    else:
        num1[a1]=num2[a+1]
print(*num1)
