
try:
    a = b;
except:
    print("Exception is caused --> NameError Exception");
    
try:
    a = b;
except NameError as ns:
    print("Named Error has occured which is a type of Exception")

    