with open("1. names_casts11.csv") as file:
    for line in file:
        name, cast = line.rstrip().split(",")
        print(f"{name}'s cast is {cast}")