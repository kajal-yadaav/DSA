def binarySearch(arr,l,r,x):
    if r>=l:
        mid=(r+l)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarySearch(arr,l,mid-1,x)
        else:
            return binarySearch(arr,mid+1,r,x)
    else:
        return -1
arr=list(map(int,input().split()))
x=int(input())
l=0
r=len(arr)-1
res=binarySearch(arr,l,r,x)
if res==-1:
    print("Number not found")
else:
    print("element "+str(x)+" found in index: "+str(res))
