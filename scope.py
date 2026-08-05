a=5       #global scope
def testing1():
    b=6     #enclosed scope
    print(a)
    print(b)
    def testing2():
        c=7     #local scope
        print(a)
        print(b)
        print(c)
    testing2()
testing1()
print(a)
print(b)    #generate error
print(c)    #genreate error