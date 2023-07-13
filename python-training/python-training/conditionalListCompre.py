# listW=[23,22,10,45,65,60,35,34,12,40]
# result=[]
# for i in listW:
#     if i%2==0:
#         if i%5==0:
#           result.append(i)
#
# print(result)

#list comprehention way
# listww=[23,22,10,45,65,60,35,34,12,40]
# result=[w for w in listww if w%2==0 ]
# print(result)

#1
# Listt=[x for x in range(1,1000) if x%7==0]
# print(Listt)

#2
# three=[x for x in range(0,1000) if '3' in str(x)]
# print(three)

# three=[x for x in range(0,100) if 3 in x]
# print(three)     #error



#3
# someString="this is Priya"
# slist=[s for s in someString if s==" "]
# print(slist)
# print(len(slist))

#4
# string="Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
# ansList=[x for x in string if x not in 'a,e,i,o,u," "']
# print(ansList)

# #5
# list=["hi",4,8.99,'apple',('t,b',"n")]


#///////
#taking inputs for python list
#
# string=input("enter the list elements")
# lst=string.split()
# print("the list is:",lst)
#
# strr="jinja"
# print(strr.split())
# # print(strr)

#get names with o
lists=["milo","bruno","bheen","krish","pranny","pr"]
res=[x for x in lists if "o" in x]
# print(res)
res2=[x for x in lists if len(x)==5]
print(res2)
print(lists.sort())





