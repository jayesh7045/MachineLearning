class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal is the class")
    def __str__(self):
        return f"{self.name}"
    def __repr__(self):
        return (f"We are dealing with the Animal {self.name}")

cat = Animal("Tom")
print(cat)
print(repr(cat))
print(dir(Animal)) # This will give us the list of the dunder methods that are available in python