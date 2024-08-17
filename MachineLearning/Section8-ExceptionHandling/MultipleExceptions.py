try:
    num = int(input("Enter a number"))
    val = 10/num
except ValueError as v:
    print(v)
    print("Valerror has occured");
except ZeroDivisionError as z:
    print(z)
    print("The Divide by zero error has occured")
else:
    print(val)
    
# IF the any of the exception from the list is caused then the else part will not executed. If any of the exception is caught then the else block will not be executed