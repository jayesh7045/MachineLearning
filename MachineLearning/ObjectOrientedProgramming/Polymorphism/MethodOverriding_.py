class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

class Cow(Animal):
    def sound(self):
        print("Moo!")

# A function that demonstrates polymorphism
def make_animal_sound(animal: Animal):
    animal.sound()

# Creating instances of different animals
dog = Dog()
cat = Cat()
cow = Cow()

# Calling the same function with different types of animals
make_animal_sound(dog)  # Output: Woof!
make_animal_sound(cat)  # Output: Meow!
make_animal_sound(cow)  # Output: Moo!
