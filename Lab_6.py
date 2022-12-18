fobj=open("D:\\D.txt","r")
s=fobj.read()
print(s)
l=s.split()
print(l)

L=[]
for i in l:
    L.append(i.strip(",.;: "))
print(L)

mx=0
for i in set(L):
    if L.count(i)>mx:
        mx=L.count(i)
        word=i
print(mx, word)
