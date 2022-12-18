#set ith bit to 1
from re import I

n=int(input())
i=int(input())
mask=1<<i
print(n|mask)