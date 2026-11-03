x = int(input("Enter x: "))

match x:
    case 1 if x > 30: # this will run if x==1 amd then the second condition matches. both must match. python checks for 1 first then it checks fot eh x > 30
        print("x is less than 30")
    case 2 if x < 40:
        print("ah, x is less than 40")

    case _ if x == 29:
        print("x is 29")
    case _:
        print("i dont know man!")

# NOW IF WE DO THIS
z = int(input("Enter z: "))
match z:
    case z if z > 1:
        print("z > 1")
    case z if z < 1:
        print("z > 1")
    case _ if z > 100:
        print("z > 1")

#this tells us that z can take any value so we must meet the second condition for the case to run 
# the pattern here in the first two cases are 1, and 2 resepectively. if the case with this pattern matches the inputted value, the code of this case will be run.