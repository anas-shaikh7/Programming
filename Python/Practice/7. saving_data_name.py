with open("3. names5.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line)



# "r": We are opening our file in read mode. This means we are loading out file not saving it. 
# readlines: lets us read all lines of the file we opened and returns the data in a list. 
# To access each value of the list lines, we use a for loop