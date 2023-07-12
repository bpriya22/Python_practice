print(type(globals()))

print(globals())

def fun(a,b):
    str1="hello"
    loc=locals()
    print(loc)
fun(10,20)