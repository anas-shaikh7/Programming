from calculator import square as sq # the program should test the code you write
import random
def main():
    test_square()


def test_square():
    n = random.randint(1, 100)
    assert sq(n) == n*n
if __name__ == "__main__":
    main()

