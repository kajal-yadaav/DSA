def maximum():
    max=list1[0]
    for i in range(l):
        if list1[i]>max:
            max=list1[i]
    return max
list1=list(map(int,input().split()))
l=len(list1)
print(maximum())
