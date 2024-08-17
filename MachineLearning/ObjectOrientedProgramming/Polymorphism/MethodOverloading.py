#In Python, you can't create two separate methods with the same name in the same class 
# (like traditional method overloading in languages such as Java or C++). 
# If you try to define multiple methods with the same name, the last method definition will 
# overwrite the previous ones.

#However, you can work around this by using different method names or by handling different numbers 
# or types of arguments within a single method, as shown previously.


# In python Method Overloading Can be performed using
class Example:
    def display(self, a=None, b=None):
        if a is not None and b is not None:
            print(f"Two arguments: a={a}, b={b}")
        elif a is not None:
            print(f"One argument: a={a}")
        else:
            print("No arguments")

# Create an instance of the Example class
example = Example()

# Call the display method with different numbers of arguments
example.display()           # Output: No arguments
example.display(10)         # Output: One argument: a=10
example.display(10, 20)     # Output: Two arguments: a=10, b=20
