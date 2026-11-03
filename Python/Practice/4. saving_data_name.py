name = input("What's your name? ")

file = open("2. names4.txt", "a")
file.write(name)
file.close()

# "a": is used tp append the name to the file 2. names.txt
# A new problem is introduced: the names are all joined together without any gap.