# y = int(input("Enter Number: "))
# print(f"y is {y}")

# ValueError: invalid literal for int() with base 10: 'cat'

# do the following to correct the error above

# try:
#     x = int(input("Enter x: "))
#     print(f"x is {x}")
# except ValueError:
#     print("Error 404. x is not a number")

# improving

# try:
#     x = int(input("Enter x: "))
# except ValueError:
#     print("Error 404. x is not a number")
# else:
#     print(f"x is {x}")

# improving
# while True:
#     try:
#         x = int(input("Enter x: "))
#     except ValueError:
#         print("Error 404. x is not a number")
#     else:
#         break
# print(f"x is {x}")

# improving 
def main():
    x = get_num()
    print(f"x is {x}")

def get_num():
    while True:
        try:
            x = int(input("Enter x: "))
        except ValueError:
            print("Error 404. x is not a number")
        else:
            break
    return x
    
main()