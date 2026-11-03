from calculator import square as sq # the program should test the code you write
import random
import pytest
def main():
    test_sq_n()
    test_sq_m()
    test_sq_o()


def test_sq_n():
    n = random.randint(1, 100)
    assert sq(n) == n*n
def test_sq_m():
    m = random.randint(1, 100)
    assert sq(m) == m*m
def test_sq_o():
    o = random.randint(1, 100)
    assert sq(o) == o*o
def test_sq_str():
    with pytest.raises(TypeError):
        sq("cat")

if __name__ == "__main__":
    main()
# if you run the pytest you would only know the first piece of code that faled not the following ones.
# to correct this you ll have to create multiple functions, which is helpful because you ll have  more clues as to what is wrong with the code.

# now we see what happens if the input is not an integer but a str. to do this i will haveto import the pytest library first. we write this code: with pytest raise A typeError if the str "cat" is squared. 