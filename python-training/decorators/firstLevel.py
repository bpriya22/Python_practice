#in pyhon , functions are considered as first class objects. Because=>
#functions in python can be passed as an arguments.


#EX1: Treating the functions as object.


# def Shout(noise):
#     return noise.upper()
#
# # print(Shout("help"))
#
# yell=Shout
# print(yell("care"))


#passing a function as a parameter


# def greet(func):
#     greeting=func("hi I'm created by function")
#     print(greeting)


# def shout(text):
#     return text.upper()

# def yell(text):
#     return text.lower()
#
# def solution(func):
#     greetings=func("Hey! iAm pRiya")
#     print(greetings)
#
# solution(shout)
# solution(yell)


#Returning functions from another functions

def adder(x):
    def mul(y):
        return x*y
    return  mul

op=adder(10)
print(op(20))

