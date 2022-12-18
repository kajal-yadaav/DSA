##def insertionsort(l):
##    for i in range(len(l)):
##        pos=i
##        while pos>0 and l[pos]<l[pos-1]:
##            l[pos],l[pos-1]=l[pos-1],l[pos]
##            pos=pos-1
##    return l;
###T(n) = O(n**2) (worst case: if the array in descending order)
###T(n) - O(n) (best case: if the array in sorted order)
##l=list(map(int,input().split()))
##l=insertionsort(l)
##print(*l)  
#--------------------------------------------
#T(n) = (n-1) +T(n-1),T(1)=1
def insertionsort(l,start,n):
    if start>=n:
        return 
    pos=start
    while pos>0 and l[pos]<l[pos-1]:
        l[pos],l[pos-1]=l[pos-1],l[pos]
        pos=pos-1
    insertionsort(1,start+1,n)
    #return l
l=list(map(int,input().split()))
l=insertionsort(l,1,len(l))
print(*l)  
