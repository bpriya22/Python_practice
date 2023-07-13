#we can use loops inside other loops->like we an use while loop inside for loop.

# i=1
# while(i<5):
#     for k in range(1,4):
#         print(i,"*",k,"=",(i*k))
#     i=i+1
#     print()

for i in range(1,6):
    k=1
    while(k<=3):
        print(i,"*",k,"=",(i*k))
        k=k+1
    print()

