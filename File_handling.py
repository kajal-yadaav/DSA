##fo1=open("D:\\a.txt","r")
##s=fo1.read(8)#return all content of file
##print(s)
##s1=fo1.read()
##print(s1)
###print(fo1.closed)
##print("Name of the file : ",fo1.name)
##print("Closed or not : ",fo1.closed) #closed: False
##print("Opening mode : ",fo1.mode) #opening mode : w

##with open("D:\\a.txt","r") as fo1:
##    s=fo1.read()
##    print(s)
##print(fo1.closed)
##f=open("D:\\a.txt","r")
##s=f.readline()
##print(s)
# Return n number of bytes as string from current position in the file

##s=f.readline(10)# return type of readline function is string 
##print(s)
##s=f.readline()
##print(s)

##l1=f.readlines()#return a list containing all rest of the lines with \n
##print(l1)

# Write function

##f=open("D:\\b.txt","w")
##s="This is demo file"
##f.write(s)
##f.close()

##f=open("D:\\demo.txt","w")
##l=["Kajal\n","Ujjawal\n","Palak\n","Astha"]
##f.writelines(l)
##f.close()

##data=open("D:\\demo.txt","r")
##s1=data.read(10)#reads the content upto 10 bytes
##print(s1)
##
##print(data.tell())
##data.readline()
##print(data.tell())

##data1=open("D:\\demo.txt","r")
##s1=data1.read()#read the content upto 10 bytes
##
##data2=open("D:\\demo1.txt","w")
##data2.write(s1) # read the content upto 10 bytes
##data2.close()

##f=open("D:\\a.jpg",'rb') # rb=read binary
##s=f.read()
##print(s)
##f.close()
##f1=open("D:\\EvtRZ_GXAAMcQKg.jpg",'wb')
##f1.write(s)
##f.close()

import os
#os.rename("D:\\demo1.txt","D:\\demo2.txt")
os.system("calc")
# Return the actual login name.
#print(os.getlogin())
# Create a leaf directory and all intermediate ones.
#os.makedirs("D:\\aa\\bb\\cc)
