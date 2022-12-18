#------------------
#SINGLE Inheritence
#------------------

class A:
    pass
class B(A):
    pass

#---------------------
#MULTI Level Inheritence
#---------------------

class A:
    pass

class B(A):
    pass

class C(B):
    pass

#-----------------------
# Hybrid Inheritence
#------------------------

class A:
    pass 
class B(A):
    pass 
class C(A):
    pass 
class D(B,C):
    pass 

