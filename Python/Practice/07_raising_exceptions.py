a = int(input("Enter the number: "))
b = int(input("Enter the number to divide by: "))

if(b == 0):
    raise ZeroDivisionError("Please enter a valid number as our program is not meant to divde by Zero")

else:
    print(f"The division of a/b is {a/b}")