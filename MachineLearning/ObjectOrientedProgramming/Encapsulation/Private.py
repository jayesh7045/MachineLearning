class Animal:
    def __init__(self, name, type, gender):
        self.name = name;
        self.type = type 
        self.__gender = gender
    def getData(self):
        return (f"Name : {self.name} Type : {self.type} Gender : {self.__gender}")

cat = Animal("Tommy", "Cat", "F")
print(cat.getData())
print(cat.name)
# print(cat.__gender)  --> This line will give us an error as __gender is a private variable
# Always note that the private variables do start with the "__"
# And the protected variables do start with the "_"
# We can also make the methods protected by using the letter "_" before the function name