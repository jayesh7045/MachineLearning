from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def description(self):
        print("This is an animal.")

# Concrete class 1
class Dog(Animal):
    def sound(self):
        print("Woof Woof")

# Concrete class 2
class Cat(Animal):
    def sound(self):
        print("Meow")

# Concrete class 3
class Bird(Animal):
    def sound(self):
        print("Chirp Chirp")

# Creating instances
dog = Dog()
cat = Cat()
bird = Bird()

# Calling methods
dog.sound()        # Output: Woof Woof
cat.sound()        # Output: Meow
bird.sound()       # Output: Chirp Chirp

dog.description()  # Output: This is an animal.
