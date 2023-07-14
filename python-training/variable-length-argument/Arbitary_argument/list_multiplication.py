# def name(**name):
#     print(type(name))
# name()
#
# def name(a,*name):
#
#     c=(5,10,15)
#
#     print("the d list is:",name)
#     print("the c list is",c)
#     res=tuple([x*y for x,y in zip(c,name)])
#     print("mul of both is :",res)
# name(1,2,3)

# def crush(*names):
#     for i in names:
#         print(i)
# crush("priya","pinky","nithya","rahul","umashankar","danish")

#program to illustrate *args with first extra argument

# def crush(arg1,*argv):
#     print(arg1)
#     for i in argv:
#         print(i)
# crush("I","miss","Jspiders","!!!")
#
# a=[1,2,3,4,5]
# b=[1,2,3,4,22]
# c=a+b
# # print(c)
# ans=[*a,*b]   #Concept of unpacking...
# print(ans)

#**kwargs  #** helps us to pass keyworded arguments...

# def myFu(**kwargs):
#     for key, val in kwargs.items():
#         print(key,val)
# myFu(a=1,b=2,c=3)

#with one extra variable

# def friends(arg1,**kwargs):
#     for x,y in kwargs.items():
#         print(x,y)
# friends("hi",nithya="nanda",priyanka="pinky",priya="rahul")

#using both *args and *kwargs in python to call a function

# def myFun(args1,args2):
#     print(args1)
#     print(args2)
#
# args=("geeks","for")
# kwargs={"args1":"priya","args2":22}
# myFun(*args)
# myFun(**kwargs)


# def myFun(*args,**kwargs):
#     print("args are:",args)
#     print("kwargs are:",kwargs)
#
# myFun("super","three","us",var1="priya",var2="good",var3="girl")

#*args take arguments as tuple..
#**kwargs take argument as dictionary.









