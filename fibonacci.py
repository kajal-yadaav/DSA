# fib(n)=fib(n-1) + fib(n-2) , fib(1)=0,fib(2)=1
#print the nth term of fibonacci series
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(5))
print(fib(7))
