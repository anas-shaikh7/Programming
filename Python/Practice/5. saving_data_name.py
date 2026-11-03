name = input("What's your name? ")

file = open("3. names5.txt", "a")
file.write(f"{name}\n")
file.close()

# Notice that the line with file.write has been modified to add a line break at the end of each name.

