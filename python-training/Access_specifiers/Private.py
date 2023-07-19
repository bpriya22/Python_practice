class Bank:
    def __init__(self,acc,balance):
        self.__acc=acc
        self.__balance=balance

    def __view(self):
        print("the acc has")
        print("the acc has : ",self.__balance)
        print(self.__acc,"is the acc no.")

bank=Bank(2567890345,20000)
bank.__view()