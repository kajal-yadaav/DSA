#modulo arithmetics
#calculate a^b (high power)

def highpower(a,b):
    res=1
    while b>0:
        if (b&1)!=0:
            res=res*a

        a=a*a
        b=b>>1

    return res

a,b=map(int,input().split())
print(highpower(a,b))
