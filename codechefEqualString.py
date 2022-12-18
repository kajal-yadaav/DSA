n=int(input())
s=input()
s1=input()
t=""
for i in range(n):
    if s[i]!=s1[i]:
        t=t+s1[i]
print((len(set(t))))
