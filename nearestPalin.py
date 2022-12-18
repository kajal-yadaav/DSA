def palin(n):
    i=n+1
    while True:
        if ispalin(i)==0:
            break
        i+=1
    return i
def ispalin(a):
    a1=str(a)
    b=a1[::-1]
    if b==a1:
        return 0
    else:
        return 1
n=int(input())
num=palin(n)
print(num)
        
