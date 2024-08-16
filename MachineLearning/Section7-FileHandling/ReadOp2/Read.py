with open("example.txt") as file:
    for line in file:
        print(line.strip()) # IF we will not use the .strip function that means a new line will be added after every line is printed
        