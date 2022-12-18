n=int(input())
a=0
b=1
print (a,b,end=" ")
n=n-2
while n>0:
    c=a+b
    print (c,end=" ")
    a=b
    b=c
    n-=1
