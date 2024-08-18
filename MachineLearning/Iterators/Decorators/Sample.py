def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# Explanation
# my_decorator(func): This is the decorator function that takes func as an argument.
# wrapper(): This is the inner function that adds behavior before and after calling func.
# @my_decorator: This syntax is a shorthand for say_hello = my_decorator(say_hello), 
# meaning that say_hello is replaced by the wrapper function returned by my_decorator.