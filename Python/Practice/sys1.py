import sys 
# WAY 1
# try:
#     print("Hello, My name is", sys.argv[1])
# except IndexError:
#     print("Insufficient Arguments")


# # WAY 2
# if len(sys.argv) < 2:
#         print("Insufficient Arguments")
# elif len(sys.argv) > 4:
#         print("Too much to Handle")
# else:
#         print("Hello, My name is", *sys.argv[1:])


# WAY 3
if len(sys.argv) < 2:
        sys.exit("Insufficient Arguments")
elif len(sys.argv) > 4:
        sys.exit("Too much to Handle") # sys.exit tells the program to exit if this condtion is not satisfied r

print("Hello, My name is", *sys.argv[1:-1])




