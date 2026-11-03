name = input("whats your name? ")
if name == "Anas":
    print("Hyderabad")
elif name == "Kako":
    print("Hyderabad")
elif name =="Poppet":
    print("Hyderabad")
elif name =="Atmoic habits":
    print("Cubby")
else:
    print("Wait for me ???")


name = input("whats your name? ").capitalize()

if name == "anas":
    print("Hyderabad")
elif name == "Mamo":
    print("Hyderabad")
elif name =="mami":
    print("Hyderabad")
elif name =="nawaz":
    print("London")
else:
    print("Wait???")


# cleaner

name = input("whats your name? ").capitalize()

if name == "Anas" or name == "Mamo" or name =="Mami":
    print("Hyderabad")
elif name == "nawaz":
    print("London")
    
else:
    print("Wait w_h_a_t???")


    # using the eyword match. Write match then the variable 
name = input("whats your name? ")
match name:
    case "anas":
        print("Hyderabad")
    case "mamo":
        print("Hyderabad")
    case "mami":
        print("Hyderabad")
    case "nawaz":
        print("London")
    case _: # we use _ for unknown values in the strings
        print("Whatever")

# even better

name = input("whats your name? ")
match name:
    case "anas" | "mami" | "mamo":
        print("Hyderabad")
    case "nawaz":
        print("London")
    case _: # we use _ for unknown values in the strings
        print("Whatever")