# def main():
#     print_column(3)

# def print_column(height):
#     # for _ in range(height):
#     #     print("#")
#     print("#\n" * 3, end="")
# main()
# def main():
#     print_row(4)

# def  print_row(width):
#     # for _ in range(width):
#     #     print("?", end="")
#     print("?" * 4)
# main()

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
main()

# improving this code
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * 3)
main()