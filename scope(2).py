a=5
def testing1():
    b=6
    print(a)
    print(b)
    def testing2():
        c=7
        nonlocal b
        global a
        b=b+10
        a=a+10
        print(a)
        print(b)
        print(c)
    testing2()
testing1()
print(a)