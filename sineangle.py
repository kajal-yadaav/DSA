from math import factorial
def sinen(n,angle):
    #iterative version
    s=0
    for i in range(n):
        s=s+pow(-1,i)*pow(angle,2*i+1)/factorial(2*i+1)
    return s
theta=float(input("enter the angle "))
radian= theta *3.14/180.0 #convert angle from degree to radian
print(sinen(50,radian))
