# Functions takes arguments which change how the functions operate
# Functions have parameters, parameters are something that you can pass to a function
# parametes and arguments are effectively the same.
# But when you use the function and input value then we call whats inside those brackets an argument.
# print(*objects, sep=' ', end='\n' file=sys flush=False)
# *objects means any number of objects(arguments) can be inside the string
# \n means next line, its a way of indicating when you want the computer to move the cursor to the next line. End shows us that by default the function is going to end its action but it doesnt as lines add up
# these parameters are optional and can be changed

name = input("Whats your name? ")

print("Hello,") #this prints hello and then name on the other line but this does not look good
print(name) # Remember this will make consecutive prints stay collectively in a box(made of same no of lines as the no of print functions) but if you add a print funtion it will be placed in its own new line 



print("Hello", end="\n") # this end="\n" is already whats default
print (name) # This end="\n" will do the same thing as above

# TO RESOLVE THIS ISSUE WE DO THIS AS WE KNOW WHATS HAPPEINING BY DEFAULT IS THIS end="\n"

print("Hello,", end="")
print(name)  # now you removed the next line parameter "\n "

#Similarly

print("Hello,",name) # print("Hello,",name, sep=" ")-- default # This automatically applies the parameter sep=" ", sep: seperator< which adds a single space. but this could be removed by doing this.

print("Hello", name, sep="") # "" shows no space --> Helloshaikh
# remember the value is stored inside a parameter
name = name.strip() # this is called a method 
# there a  lot of functions in python and heir functionality can be assesed by using this 