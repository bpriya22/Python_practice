# print("hello")

#the below method is by using "loops"
# h_letter=[]
# for  letter in "human":
#     h_letter.append(letter)
# print(h_letter)

#using list comprehension
#iterating through a string using list comprehension
#
# hello=[]
#
# hello=[letter for letter in "byeee"]
# print(hello)
#
# list22=[]
# listNew=[x for x in range(50) if x % 2==0]
# print(listNew)

listY=[x for x in range(100) if x%2==0 if x%5==0]
print(listY)

listZ=["even" if x%2==0 else "odd" for x in range(10)]
print(listZ)