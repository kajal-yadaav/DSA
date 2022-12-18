#Pattern Program
#1 Pyramid
def pyramid(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
pyramid (5)

#Inverse Pyramid
def inversepyramid(n):
    k=2*n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
inversepyramid (5)

#right start pattern 
#left start pattern

#hour glass Pattern
def hourpattern(n):
    k=n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
    k=2*n-2
    for i in range(0,n+1):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
hourpattern(5)

#right triangle
#left triangle
#diamond pattern

#diamond star pattern
for i in range(5):
    for j in range(5):
        if i+j==2 or i-j==2 or i+j==6 or j-i==2:
            print("*",end="")
        else:
            print(end=" ")
    print()