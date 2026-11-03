names = []

with open("3. names5.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print("Hello,", name)


# Notice that names is a blank list where we can collect the names. Each name is appended to the names list in memory. Then, each name in the sorted list in memory is printed. Running your code, you will see that the names are now properly sorted.
# if you are opening a file to readi it, you donbt need to specify "r"