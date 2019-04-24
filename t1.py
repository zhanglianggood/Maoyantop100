def g():
    print("1")
    x = yield "hello"
    print("2,x = ", str(x))
    y = 5 + (yield x)
    print("3,y = ", str(y))


f = g()
print(f)
print(f.__next__())
f.send(5)
#print(f.__next__())
f.send(10)
#print(f.__next__())