f1=open("temp.txt","r")
r=f1.read()
print(r)

w=input("enter the string")
f1=open("temp.txt","w")
f1.write(w)
f1.close()

f1=open("temp.txt","r")
r=f1.read()
print(r)
