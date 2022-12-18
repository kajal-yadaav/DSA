#square root of a number by newton's method
x=2
a=327
while 1:
    xnew=0.5*(x+a/x)
    if abs(xnew-x)<0.001:
        break
    x=xnew
print("with value: ",x)

