#class method / static method  / instance method

class MyClass:
    def __int__(self,value):
        self.value=value

    @staticmethod
    def get_max_value(x,y):
        return max(x,y)

# create an instance of my class
obj=MyClass(10)

print(MyClass.get_max_value(12,13))


print(obj.get_max_value(20,30))
