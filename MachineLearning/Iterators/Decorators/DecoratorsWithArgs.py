def my_dec(n):
    def Wrapper(fun):
        def new_fun(*args, **kwargs):
            for i in range(n):
                print(i)
            return fun(*args, **kwargs)  # Call the decorated function with args and kwargs
        return new_fun
    return Wrapper

@my_dec(4)
def say_hello():
    print("Hello")

say_hello()
