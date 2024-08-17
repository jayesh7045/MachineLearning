try:
    file = open("example.txt", "r")
    content = file.read();
    print(content)
except FileNotFoundError as f:
    with open("example.txt", "w") as filee:
        pass
    print(f)
    print("File does not exists")
finally:
    if not file.closed:
        file.close();
        print("The file is successfully closed now")
     