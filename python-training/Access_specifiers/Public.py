class Geek:
    #constructor
    def __init__(self,name,age):
        #public data member
        self.geekName=name
        self.geekAge=age

    #public member function
    def displayAge(self):

        print("Age: ",self.geekAge)

obj=Geek("Akshay",27)

#accessing public data member
print("Name:",obj.geekName)

#accessing public member function of the class
obj.displayAge()