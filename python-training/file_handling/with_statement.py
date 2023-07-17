#with statement=> It automatically closes the file.


# with open("demo.txt","r") as f:
#     content=f.read()
#     print(content)

# with open("demo.txt","w") as f:
#     content=f.write("hello nithya!")
#     print(content)


#WRITING
# with open("demo1.txt","w") as p:
#     content=p.write("this is new one! ")
#     print(content)
#
#APPENDING
# with open("demo1.txt","a") as g:
#     g.write("Lol! became old now!")
#     print("done!!")

#READING
with open("demo1.txt","r") as q:
    x= q.read()
    print(x)
    print("done...")




