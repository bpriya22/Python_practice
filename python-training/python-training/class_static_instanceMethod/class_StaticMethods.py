from datetime import date

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age



    @classmethod   #acts as an alternative constructor-> which takes name and year as parameter
    def fromBirthYear(cls,name,year):   #----> this is a class method /Acts as an alternative constructor
        #here, the parameter cls represent the class person.
        return cls(name,date.today().year-year)   #->newly created object.

    @staticmethod  #this is a static method that does n't depend on class or instance state.
    def isAdult(age):
        return age>18

person1=Person("Priya",22)
person2=Person.fromBirthYear("karthik",1992)  #object created using the "from birth year" class method.

print(person1.age)
print(person2.age)

print(Person.isAdult(31))

