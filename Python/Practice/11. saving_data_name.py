
with open("3. names5.txt") as file:
    for line in sorted(file, reverse=True):
       print("Hello,", line.rstrip())


# This is much shorted
# It is not helpful if you want to introduce multiple changes.
# to play with this a little we have revrsed the alphabetic order like from Z to A.
# to do these things you need to look at the documentation and alter the default values


















# What if we wanted the ability to store more than just the names of students? What if we wanted to store both the student’s name and their cast as well?
# We make the use of CSV(comma seperated values) for this purpose