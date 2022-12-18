#find nth number of bit
a=int(input())
n=int(input())
a1=a
S=""
n1=1
while a1>0:
    if a1%2==0:
        S="0"+S
    else:
        S="1"+S
    a1=a1>>1
n1=1<<n
if n1&a==0:
    print("bit is 0")
else:
    print("bit is 1")