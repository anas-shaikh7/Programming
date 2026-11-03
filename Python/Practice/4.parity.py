x = int(input("Whats x? "))

if x % 2 == 0:
    print("x is even")
else: #--> x % 2 == 1
    print("x is odd")



def main():
    x = int(input("Enter x: "))
    checking(x)
    print(checking(x))


def checking(evenodd):
    if evenodd % 2 == 0:
        return "x is even"
    else: 
        return "x is odd"
    
main()


def main():
    x = int(input("Give me x: "))
    if checking_even(x):
        print("Even")
    else: 
        print("Odd")

def checking_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()

#making this more pythonic . these are called the pythonic rexrpessions

def main():
    x = int(input("Please give x: "))
    if checking_even(x):
        print("Even")
    else: 
        print("Odd")

def checking_even(n):
    return True if n % 2 == 0 else False


main()
# even more pythonic
def main():
    x = int(input("Give me x: "))
    if checking_even(x):
        print("Even")
    else: 
        print("Odd")

def checking_even(n):
    return n % 2 == 0 # this is the condtion. “If a condition is true, Python evaluates it as True. If it’s not true, it evaluates as False.”
# this works because its only gonna be true when the remainder is 0, so we dont need to write if else. this  function is itself a boolean expression. So it is just gonna return the bools(true or false)

# Step 1: Input
# Give me x: 6

# Python converts:

# "6" → 6

# So:

# x = 6
# Step 2: Function call
# checking_even(6)
# Step 3: Inside function
# Calculation:
# 6 % 2 = 0
# Comparison:
# 0 == 0 → True
# Return value:
# True
# Step 4: Back to if
# if True:

# So Python runs:

# print("Even")
# ✅ OUTPUT
# Even