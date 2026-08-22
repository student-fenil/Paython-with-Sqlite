#read
f1=open("temp.txt","r")
r=f1.read()
print(r)


#write
f1=open("temp.txt","w")
f1.seek(2)
w=input("enter the string:")
f1.write(w)
f1.close()

#append
f2=open("testfile.txt","a")
f2.write('welcome')
f2.close()

#read append
f3=open("textfile.txt","r")
r=f3.read()
print(r)
