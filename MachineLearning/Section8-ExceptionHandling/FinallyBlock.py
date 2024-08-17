try:
    a = b 
except NameError as n:
    print(n)
    print("The name Error has occured")
else:
    print("No excp")
finally:
    print("This is the block which is executed every time, no matter the exception has occured or not")
    

# The else block will be executed only if the exception is not occured
# The finally block will be executed, no matter if the exception is occured or not
    