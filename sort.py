def sort(arr):
    pivot=0
    j=0
    for i in range(len(arr)):
        if arr[i]<pivot:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr
arr=[9,-3,5,-2,-8,-6,1,2]
sort(arr)
for k in range(len(arr)):
    if arr[k]>0:
        break
print(k)
i=0
while i<=len(arr)-2:
    arr[i],arr[k]=arr[k],arr[i]
    i+=2
    k+=1
print(arr)
    
    
