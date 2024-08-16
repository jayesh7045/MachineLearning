import os
file = "example.txt"
if os.path.exists(file):
    print("The example.txt is a file")
else:
    print(os.path.abspath(file)) # This will also create a file if it does not exists and will return the abs path
    with open("example.txt", 'w') as file:
        pass


if(os.path.isdir(file)):
    print("Its a dir")
elif(os.path.isfile(file)):
    print("Its not a dir but a file")
