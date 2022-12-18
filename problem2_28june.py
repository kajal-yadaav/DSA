def evenoddsum(n,S,S1,ind):
    a=str(n)
    if n<=(pow(10, n)-1):
        if ind==s:
            if S==S1:
                print(n)
                
            S=0
            S1=0
            ind=0
        elif ind%2==0:
            S+=int(a[ind])
        elif ind%2!=0:
            S1+=int(a[ind])
        evenoddsum(n+1,S,S1,ind+1)
    else:
        return 
    
s=int(input())
n=int(pow(10, s-1))
evenoddsum(n,0,0,0)
