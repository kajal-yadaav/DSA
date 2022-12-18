#clear ith bit to 1

n=int(input())
i=int(input())
mask=~(1<<i)
print(n&mask)