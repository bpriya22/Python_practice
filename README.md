# Python_practice
practice python programming.
python learning.

websites help:
https://www.tutorialspoint.com/python/index.htm
https://pynative.com/python-exceptions/


practice exercises:
https://pynative.com/python-exercises-with-solutions/


reference for Python File Handling and Python Modules:
https://www.javatpoint.com/python-modules


creating and accessing a python package:
https://www.tutorialspoint.com/create-and-access-a-python-package


creating a package and installing it:
https://www.tutorialsteacher.com/python/python-package

installing package globally:
once a package is created it can be installed globally..
https://www.tutorialsteacher.com/python/python-package



You may also want to publish the package for public use. PyPI (stands for Python Package Index) is a repository of Python packages. Visit https://packaging.python.org/distributing to know more about the procedure of uploading a package to PyPI.



polymorphism:
https://www.geeksforgeeks.org/polymorphism-in-python/


OOPs concept:
refered: LCO -HC


Documentation to be refered:
1.  https://docs.python.org/3/library/sqlite3.html

2.  https://pypi.org/



* CLASS METHODS, STATIC METHODS:

from datetime import date

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age



    @classmethod   #acts as an alternative constructor-> which takes name and year as parameter
    def fromBirthYear(cls,name,year):   #----> this is a class method /Acts as an alternative constructor
        return cls(name,date.today().year-year)   #->newly created object.

    @staticmethod  #this is a static method that does n't depend on class or instance state.
    def isAdult(age):
        return age>18

person1=Person("Priya",22)
person2=Person.fromBirthYear("karthik",1992)  #object created using the "from birth year" class method.

print(person1.age)
print(person2.age,person2.name)

print(Person.isAdult(31))



The code provided defines a Person class with an alternative constructor fromBirthYear as a class method and a static method isAdult. Let's go through the code and the output:

Two instances of the Person class are created: person1 and person2.

person1 is created directly by providing the age parameter as 22.

person2 is created using the fromBirthYear class method, where the birth year is provided as 1992. The method calculates the age based on the current year (using date.today().year) and returns the Person object with the calculated age. person2 will have the name "karthik" and age based on the current year.

The age attribute of person1 and person2 objects is printed. The age of person1 is 22, and the age of person2 is calculated based on the birth year 1992 and the current year when the code is executed. Therefore, the age of person2 will depend on the current year, and it could be different each time you run the code.

The name attribute of person2 is also printed. The name of person2 is "karthik".

The isAdult static method is called with an age parameter of 31, and the result (True or False) is printed. Since the age provided (31) is greater than 18, the output will be True.

Note: The ages and the name of the persons in the output might differ depending on the current year when the code is executed.



=>what does cls mean in the class method 
and it returns cls object, what does that mean.


@classmethod
def fromBirthYear(cls, name, year):
    return cls(name, date.today().year - year)

    

The @classmethod decorator indicates that the method is a class method.

The first parameter of the fromBirthYear method is cls, which represents the class Person itself. When the method is called, Python automatically passes the class as the first argument, just like self is passed to instance methods.

The fromBirthYear class method takes two additional parameters, name and year, which are used to create a Person object with the calculated age.

Inside the method, cls(name, date.today().year - year) is used to create a new instance of the class (Person). It calls the constructor (__init__ method) of the class Person, passing name and the calculated age (date.today().year - year) as arguments. This creates a new Person object with the provided name and age.

So, when you call Person.fromBirthYear("karthik", 1992), it creates a new Person object with the name "karthik" and the age calculated based on the birth year 1992 and the current year. The cls in this case refers to the Person class, and it is used to create an instance of the class.

By using a class method, you can provide an alternative way to create objects, in this case, by specifying the birth year instead of directly providing the age. It helps to encapsulate the logic of object creation and can be particularly useful when you have multiple ways to construct objects or need to perform additional computations during object creation.


ACCESS SPECIFIERS (ACCESS MODIFIERS)

https://www.geeksforgeeks.org/access-modifiers-in-python-public-private-and-protected/

https://www.tutorialspoint.com/access-modifiers-in-python-public-private-and-protected


MAGIC METHODS IN PYTHON

https://www.tutorialsteacher.com/python/magic-methods-in-python

