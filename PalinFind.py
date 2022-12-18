n=input()
n1=n[::-1]
while True:
    sum=int(n)+int(n1)
    if str(sum) == str(sum)[::-1]:
        print(sum)
        break
    n=sum   
    n1=str(sum)[::-1]
