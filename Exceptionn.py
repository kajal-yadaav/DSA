try:
    print(7/0)
    print(int('4'))
    l=[2,3,4]
    print(l[3])
except (ValueError , ZeroDivisionError , IndexError) as e:
    print("some error generated ",e)
else:
    print("code successfully executed")
finally: 
    print("Compulsory execution")
print("we can still continue")
print("psit")
