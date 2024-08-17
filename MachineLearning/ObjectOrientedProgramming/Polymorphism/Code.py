class Animal:
    def __init__(self, name) -> None:
        self.name = name
        print("The Object of the Animal Class is created")
    def sound():
        print("Woof!")


class Dog(Animal):
    def __init__(self, name, type)->None:
        super().__init__(name)
        self.type = type
        print("Dog is invoked")
        print(self.name+" Kutta Hai")
        
An = Dog("Sanjiv Roy", "Dog")
print(An.type)