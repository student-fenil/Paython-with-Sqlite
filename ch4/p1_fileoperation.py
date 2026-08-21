f1=open("temp.txt", "r")
r = f1.read()
print(r)
f1.close()

w = input("Enter the string: ")

f1 = open("temp.txt", "w")
f1.write(w)
f1.close()

f1 = open("temp.txt", "r")
r = f1.read()
print(r)
f1.close()