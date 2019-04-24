
a = int(input("a "))
b = int(input("b "))
c = int(input("c "))

if a < b and a < c :
    print(a, "a")
    if b < c:
        print(b, "b")
        print(c, "c")
    else:
        print (c, "c")
        print (b, "b")
elif b < a and b < c:
    print(b, "b")
    if a < c:
        print (a, "a")
        print (c, "c")
    else:
        print (c, "c")
        print (a, "a")
        if a < b:
            print (b, "b")
            print (a, "a")
