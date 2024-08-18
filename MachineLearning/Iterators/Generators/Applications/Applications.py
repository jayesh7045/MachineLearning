# Generators are used to read and access the data from a large files as the large file contains a lot of data which is 
# in particular not helpful at the current situation

# They help us to read and process the data of the file, one line at a time

def open_file_using_generators(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line


Generator_Object = open_file_using_generators("generator_file.txt")
for i in Generator_Object:
    print(i.strip())