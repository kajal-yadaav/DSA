n=int(input())
S=""
while n>0:
    if n%2==0:
        S="0"+S
    else:
        S="1"+S
    n=n//2
print(S)