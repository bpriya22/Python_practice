class Student:

    _name=None
    _roll=None
    _branch=None

    def __init__(self,name,roll,branch):
        self._name=name
        self._roll=roll
        self._branch=branch

    def _displayRollNum(self):
        print("Roll:",self._roll)
        print("Branch",self._branch)

class Geek(Student):

    def __init__(self,name,roll,branch):
        #Student.__init__(self,name,roll,branch)
        super().__init__(name,roll,branch)

    def displayData(self):
        print("name:",self._name)
        self._displayRollNum()

obj=Geek("priya",969,"ise")
obj.displayData()

