import os
file_path = "file1.txt"
folder_path = "Folder"
relative_path = os.path.join(file_path, folder_path) # this is the relative path
absolute_path = os.path.join(os.getcwd(), folder_path, file_path);
print(absolute_path)
print(relative_path)