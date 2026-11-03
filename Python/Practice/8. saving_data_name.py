with open("3. names5.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line.rstrip())


# This method creates a problem that there is a line break after each line of output
# To correct this, we use rstrip.