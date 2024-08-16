## w+ mode is used to open up the file in reading as well as the writing and if the file does not exists then the file will be created
with open("example.txt", "w+") as file:
    file.write("Hello World")
    file.seek(0)
    content = file.readline();
    print(content)
    
    
# Always note that, whenever we open a file and write something into it, the file pointer after writing is at the end of the file. And during reading we have to make the file pointer to 0 using seek(0) and then perform the read operation
