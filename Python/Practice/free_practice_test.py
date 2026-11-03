from free_practice import cube
import random
import pytest

def main():
    # test_cube() 
    test_cube_way3_1()
    test_cube_way3_2()
    test_cube_way3_3()

# def test_cube():
# WAY 1
    # n = random.randint(1, 100)
    # if cube(n) == n*n*n:
    #     print("You are good to go!")
    # else:
    #     error_number = ["404", "504", "911"]
    #     error = random.choice(error_number)
    #     print("Error", error)
# WAY 2
    # n = random.randint(1, 100)
    # assert cube(n) == n*n*n    
# WAY 3
def test_cube_way3_1(): 
    a = random.randint(1, 100)
    assert cube(a)  == a*a*a    

def test_cube_way3_2(): 
    b = random.randint(1, 100)
    assert cube(b)  == b*b*b
    
def test_cube_way3_3(): 
    c = random.randint(1, 100)
    assert cube(c) == c*c*c
    



# WAY 3
if __name__ == "__main__":
    main()