# a=[1,2,3]
# b=[2,3,4]
# c=[x*y for x,y in zip(a,b)]
# print(c)
# list1=["priya","nithya","pinky"]
# list2=["rahul","saish","uma"]
# list3=zip(list1,list2)
# print(list3)

x=[1,2,3,5,6]
y=[3,5,7]
c=[]
if len(x)==len(y):
  for i,j in zip(x,y):
     c.append(i*j)
else:
    print("no way!")
print(c)
