lines = ["My name is", "Jayesh Harish", "Wadhwani"];
with open("example.txt", 'w') as file:
    file.writelines(lines)
    