#INHERITANCE
class Samsung:
    "constructor"
    def __int__(self):
        print("I am Samsung")

    def makeScreen(self):
        print("I make screens")
        print("i make screens : Samsung")

    def test(self):
        print("Screen test: OK")

class Iphone(Samsung):

    "constructor"
    def __int__(self):
        print("I am Iphone")
        # super().__int__()

    def a3chips(self):
        print("I make A3 bionic chips")

    def itest(self):
        print("A3 test: OK")
        super().test() # also includes the test done(block) of code implemented in Samsung.

    def makeScreen(self):
        print("I make screen: Apple")   #METHOD OVERIDING

user=Iphone()
# user.a3chips()
# user.itest()
user.makeScreen()


