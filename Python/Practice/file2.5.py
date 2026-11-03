#continuing definign functions 

# remember if a function is called first and it is defined later, the function will not run because the system  requires the defination of the function first
def main():
    name = input("whats ur name? ")
    random(name)

def age():
    yearsold = input("Whats ur age? " )
    random(yearsold)

def random(call="world"):
    print("I am", call,)

age()


def main2():
    y = int(input("whats y? "))
    print("y cubed is", cubed(y))

def cubed(n):
    return n ** 3 # or n * n * n or pow(n , 3)


main2()