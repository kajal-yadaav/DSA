#------LIST COMPREHENSIVE-------#
L=[x*x for x in range(1,11)]
print(L)
L=[x*x for x in range(1,11) if x%2==0]
print(L)
l=[3,6,2,7]
L=[i*2 for i in l]
print(L)
l=[3,2,4,1]
L=[e*2 for e in [item+1 for item in l]]  #Nested list
print(L)


#------packing---------#

