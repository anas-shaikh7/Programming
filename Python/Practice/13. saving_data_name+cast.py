with open("1. names_casts11.csv", "w") as file:
    for _ in range(3):
        name_cast = input("What's your name & cast? ")
        file.write(f"{name_cast}\n")
    
    



























# What if we wanted the ability to store more than just the names of students? What if we wanted to store both the student’s name and their cast as well?
# We make the use of CSV(comma seperated values) for this purpose