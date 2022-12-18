def selection_sort(l):
    for i in range(len(l)):
        min=i
        for j in range(i+1,len(l)):
            if l[j]<l[min]:
                min=j
        l[min],l[i]=l[i],l[min]
    return l
l=list(map(int,input().split()))
l=selection_sort(l)
print(*l)  
