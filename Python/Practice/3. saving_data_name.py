name = input("What's your name? ")

file = open("1. names3.txt", "w")
file.write(name)
file.close()






# Open is a function built into python thats allows you to open a file and utilize it in your program, such that you can read from it(means read saved data) or write to it. The file you open is called a file I/O.
  
# Notice that the open function opens a file called names.txt with writing enabled, as signified by the w. The code above assigns that opened file to a variable called file. The line file.write(name) writes the name to the text file. The line after that closes the file.

# However, if you run your program multiple times using different names, you will notice that this program will entirely rewrite the names.txt file each time
