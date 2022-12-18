#deadline
m=int(input())
task=[0]*m 
deadline=[0]*m 
profit=[0]*m
for i in range(m):
    task[i],deadline[i],profit[i]=map(int,input().split())

for i in range(m):
    for j in range(0,m-1-i):
        if profit[j]<profit[j+1]:
            profit[j],profit[j+1]=profit[j+1],profit[j]
            task[j],task[j+1]=task[j+1],task[j]
            deadline[j],deadline[j+1]=deadline[j+1],deadline[j]

maximum=max(deadline)

maxx=[-1]*maximum

for i in range(maximum):
    if maxx[task[i]-1]==-1:
        maxx[task[i]]=profit[i]
    else:
        j=task[i]-2
        while j>=0:
            if maxx[j]==-1:
                maxx[j]=task[i]
            j-=1
        if j<0:
            break 

for i in range(m):
    print(task[i],deadline[i],profit[i],end=" ")
    print()

print(sum(maxx))