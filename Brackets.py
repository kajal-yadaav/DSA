s=input()
l=['']*len(s)
j=0
f=0
for i in s:
    if i=='(' and l[0]=='':
        l[0]=i
        j+=1
    elif i=='{' and l[0]=='':
        l[0]=i
        j+=1
    elif i=='[' and l[0]=='':
        l[0]=i
        j+=1
    elif i=='(' and (l[j-1]=='(' or l[j-1]=='[' or l[j-1]=='{'):
        l[j]=i
        j+=1
    elif i=='{' and (l[j-1]=='(' or l[j-1]=='[' or l[j-1]=='{'):
        l[j]=i
        j+=1
    elif i=='[' and (l[j-1]=='(' or l[j-1]=='[' or l[j-1]=='{'):
        l[j]=i
        j+=1
    elif i==')' or i=='}' or i==']':
        if i=='(' and (l[j-1]=='('):
            l.pop()
            j-=1
        elif i=='[' and (l[j-1]==']'):
            l.pop()
            j-=1
        elif i=='{' and (l[j-1]=='}'):
            l.pop()
            j-=1
        else:
            f=1
            break

if len(l)==0 and f==0:
    print("YES")
else:
    print("NO")


##s=input()
##l=[0]*6
##if '(' in s:
##    l[0]=s.count('(')
##if ')' in s:
##    l[1]=s.count(')')
##if '{' in s:
##    l[2]=s.count('{')
##if '}' in s:
##    l[3]=s.count('}')
##if '[' in s:
##    l[4]=s.count('[')
##if ']' in s:
##    l[5]=s.count(']')
##if l[0]==l[1] and l[2]==l[3] and l[4]==l[5]:
##    print("YES")
##else:
##    print("NO")
##    
