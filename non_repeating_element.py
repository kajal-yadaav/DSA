#find the two non repeating element in an array where every element repeats twice
n=list(map(int,input().split()))
S=n[0]
for i in n[1:]:
    S=S^i
print(S)