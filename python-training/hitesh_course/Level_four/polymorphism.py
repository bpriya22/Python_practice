class Animal:
    def speak(self):
        raise NotImplementedError("subclass must implement this method..")

class Dog(Animal):
    def speak(self):
        return "woof!"

class cat(Animal):
    def speak(self):
        return "meow"

animals=[Dog(),cat()]

for animal in animals:
    print(animal.speak())