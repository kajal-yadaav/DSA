f1=open("D:\\test.txt","w")
with open("D:\\test.txt","r") as myfile:
    data=myfile.readlines()
data1=data[::-1]

f1.writelines(data1)

f1.close()
