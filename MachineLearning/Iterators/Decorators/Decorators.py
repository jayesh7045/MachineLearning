def my_dec(fun):
    def wrapper():
        print("Inside the Wrapper class")
        fun()
        print("Outside the wrapper class")
    return wrapper

@my_dec
def say_hello():
    print("Hello")

say_hello()

# Here is an example of the decorator in python