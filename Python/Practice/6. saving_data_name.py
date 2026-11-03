name = input("What's your name? ")

with open("3. names5.txt", "a") as file:
    file.write(f"{name}\n")


# The keyword with allows you to automate the closing of a file.

