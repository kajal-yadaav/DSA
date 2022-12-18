#find the smallest missing positive number from an unsorted array in O(n) time complexity
l=list(map(int,input().split()))
f=0
i=1
while f!=1:
    if i not in l:
        f=1
    i+=1
print(i-1)
5
