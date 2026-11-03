# Open will create a file for me named names.txt and the w inside open will allow me to write there. The open function returns something called the file handle, whihch is a special values that gives access to the file subsequently.

name = input("Was ihr name? ")

file = open("name_file1.txt", "w") # This will only store the name for now and remove it later.
file.write(name) 
file.close()

file = open("name_file2.txt", "a") # This will append the name inputted and store it in the name_file2.txt
file.write(f"{name}\n") # file.write(f"{name}") will write the append the name in line w/o space. 

with open("name_file2.txt", "a") as file:
    file.write(f"{name}\n") 
# This is a more pythonic way of writing the same code because there is no need to close the file. +

