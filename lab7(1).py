def linear(l,n):
    for i in range(len(l)):
        if l[i]==n:
            return i
l=list(map(int,input().split()))
n=int(input())
i=linear(l,n)
print("element "+str(n)+" is at index: "+str(i))
