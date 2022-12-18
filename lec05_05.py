s="this is python lab in lab"
print(s.endswith("ab"))
print(s.startswith("thi"))
print(s.count("is"))
print(s.count("is",7,15))#count no of "is" between index 7 to 15
print(s.find("is"))
print(s.index("is"))
print(s.rfind("is"))# if the actual string does not exist it return -1
print(s.rindex("is"))#if string not present print the valueerror
str="pythonlab"
print(str.isalpha())
#str="python lab"
#print(str.isalpha())#print error because of space char
#st="hello"
#print(s.zfill(10))
#strip(var) function remove whitespace if n
print("a\tb\tc".expandtabs(20))
