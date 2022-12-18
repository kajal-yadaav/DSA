print("Python")
try:
    print(int('a'))
except ValueError:
    print("hello")
print("we can still continue")
print("psit")
print("python")
try:
    print(a)
    print(int('a'))
except ValueError:
    print("hello")
except:
    print("some exception generated")
print("we can still continue")
print("psit")

#when the else block of exception handling is executed whenever no exception is generated in the program
#finally clause will be executed whether the exception is generated or not hence it will always be executed

try:
    print(7/0)
    print(int('4'))
    l=[2,3,4]
    print(l[3])
except Exception as e:
    print("Some problem occured",e)
except ValueError as e:
    print("some wrong value exception generated:",e)
except ZeroDivisionError as e:
    print("some exception generated:",e)
else:
    print("code successfully executed")
finally: 
    print("Compulsory execution")
print("we can still continue")
print("psit")
