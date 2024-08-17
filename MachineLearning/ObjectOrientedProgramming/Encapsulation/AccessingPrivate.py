class Animal:
    def __init__(self, name: str, age: int):
        self.__name = name  # Private variable
        self.__age = age    # Private variable

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

# Creating an instance of Animal
animal = Animal("Leo", 4)
animal.display_info()

# Trying to access private variables directly (this will raise an AttributeError)
# print(animal.__name)  # Uncommenting this line will raise an AttributeError

# Accessing private variables using name mangling (not recommended)
print(animal._Animal__name)  # This works but breaks encapsulation
print(animal._Animal__age)
