class Car:
    
    def __init__(self, name, wheels, windows):
        self.name = name
        self.wheels = wheels
        self.windows = windows
    def drive(self):
        print("The car "+self.name + " is driving")
        
        
audi = Car("Audi", 4, 2)
print(audi.windows)
print(audi.wheels)
print(audi)
audi.drive()