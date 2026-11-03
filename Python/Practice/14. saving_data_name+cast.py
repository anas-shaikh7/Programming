with open("1. names_casts11.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]}'s cast is {row[1]}")