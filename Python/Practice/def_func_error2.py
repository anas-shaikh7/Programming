# def main():
#     x = get_num()
#     print(f"x is {x}")

# def get_num():
#     while True:
#         try:
#             x = int(input("Enter x: "))
#         except ValueError:
#             print("Error 404. x is not a number")
#         else:
#             break
#     return x
    
# main()


#improving
# def main():
#     x = get_num()
#     print(f"x is {x}")

# def get_num():
#     while True:
#         try:
#             x = int(input("Enter x: "))
#         except ValueError:
#             print("Error 404. x is not a number")
#         else:
#             return x
    
# main()
# improving
# def main():
#     x = get_num()
#     print(f"x is {x}")

# def get_num():
#     while True:
#         try:
#             x = int(input("Enter x: "))
#             return x
#         except ValueError:
#             print("Error 404. x is not a number")
    
# main()
# #improving
# def main():
#     x = get_num()
#     print(f"x is {x}")

# def get_num():
#     while True:
#         try:
#             return int(input("Enter x: "))
#         except ValueError:
#             print("Error 404. x is not a number")
    
# main()
#improving
# def main():
#     x = get_num()
#     print(f"x is {x}")

# def get_num():
#     while True:
#         try:
#             return int(input("Enter x: "))
#         except ValueError:
#             pass
    
# main()

#improving
def main():
    x = get_num("Enter x: ")
    print(f"x is {x}")

def get_num(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
    
main()