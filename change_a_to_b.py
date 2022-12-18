#count how many operation needed to change a to b
#a=10101
#b=11011
#output=3
n=int(input())
n1=int(input())
S=n^n1
c=0
while S!=0:
    S=S&(S-1) # if S=1101 the by doing this S becomes 1100 then again become 1000
    c+=1
print(c)