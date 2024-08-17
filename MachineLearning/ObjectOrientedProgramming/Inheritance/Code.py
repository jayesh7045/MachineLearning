class Vehicle:
    def __init__(self, name):
        print("The Constructor of the Vehicle Class is called")
        self.name = name 
    def What_is_Vehicle_name(self):
        return self.name


class Car(Vehicle):
    def __init__(self, name, type):
        self.type = type
        self.name = name
    def printData(self):
        return ("The Vehicle name is "+self.name+" and the type is "+self.type)


audi = Car("BMW", "Car");
print(audi.printData());
         