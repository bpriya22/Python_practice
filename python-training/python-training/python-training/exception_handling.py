
#1...
# try:
#     print(x)
#     def sayhi():
#       print("say hi!!!")
#     sayhi()
# except:
#    print("an exception occured!")  #Since the try block raises an error the except block is executed..
   #withhout try block the program might have crashed with an error

#2...
#can have as many exception blocks as we need..
#special exception for special kind of error.

# print(x)  #NameError.-> returns

#->

# try:
#     print(x)
# except NameError:
#     print("variable x is not defined!!" )
# except:
#     print("something else went wrong!!")   #default except must be at the last..this is called default except..

# try:
#     print("x")
# except:
#     print("something went wrong!!")
# else:
#     print("nothing went wrong!!")


#finally
#finall block executes regardless to try block catches an error or not..

# try:
#     print("hello")
# except NameError:
#     print("value not defined!")
# except:
#     print("error occured!")
# finally:
#     print("executes regardlessly")

# try:
#     f=open("demofile.txt","w")
#     try:
#         f.write("lorem ipsum")
#
#     except:
#         print("something went wrong while writing the file!")
#     finally:
#         f.close()
# except:
#     print("something went wrong when opening the file..!")
# finally:
#     print("executed anyway!")

#Raise an exception

# x=-1
# if x<0:
#     raise Exception("sorry no numbers below 0")
# #"the raise keyword is used to raise an exception"

x="hello"
if not type(x) is int:
    raise TypeError("only integers are allowed..")














