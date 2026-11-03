identities = []

with open("1. names_casts11.csv") as file:
    for line in file:
        name, cast = line.rstrip().split(",")
        identities.append(f"{name}'s cast is {cast}")

for identity in sorted(identities):
    print(identity)
