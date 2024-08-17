from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        return "kui"
    
class Cat(Animal):
    def __init__(self) -> None:
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"


tom = Cat();
gi = Dog();
print(tom.sound())
print(gi.sound())


# The issue you're encountering is due to the fact that methods in Python classes, 
# including those in subclasses, need to have self as the first parameter if they're 
# instance methods. This is true for methods defined in a class that inherits from ABC.

# Always pass the self as the params in the instance level functions

# If we are defining the function as the abstractMethod in the abstract Class, then we have to define it in the class inheriting it
