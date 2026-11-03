from calculator import square as sq # the program should test the code you write
import random
def main():
    test_square()


def test_square():
    n = random.randint(1, 100)
    if sq(n) != n*n:
        print(f"ERROR: {n} square was NOT {n*n}")
    else:
        print("Your code is correct!")

if __name__ == "__main__":
    main()
    