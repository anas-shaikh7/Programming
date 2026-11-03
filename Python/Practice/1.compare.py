x = int(input("whats x? "))
# input("whats x? ") runs first
#→ it returns a string(str) (always), like "5"
#int(...) then takes that string
#→ converts it into an integer, like 5
#That integer is stored in x(copied to x from the right)
y = int(input("Whats y? "))


if x < y:
    print("X is less than Y") # this identiation at the left tells python this line will only run if the above statement is true.
    # press tab to indent
if x > y: 
    print("x is grester than y")

if x == y: 
    print("x is equal to y")

# this 3 ifs mean that keep asking questions and answer them aswell until you reach the end. but this is inefficient. We should ask question at a time and proceed to stop if that condition is true or the answer to that questikn is correct. if its not true we should continue asking more questions and stop as soon as we get meet the condition.
# to achieve this we do the following 
if x < y:
    print("X is less than Y") 
elif x > y: 
    print("x is grester than y")

elif x == y: 
    print("x is equal to y")

# elif just means ask this question if the previous condition is false
# but this method is also less efficient because its logical if x is not greater than or lesser than y it must be equal to y. so we dont need to ask another question. we can end the program then and there.

if x < y:
    print("X is less than Y") 
elif x > y: 
    print("x is grester than y")

else: # else x == y: is wrong because its logical and you dont have more questions
    print("x is equal to y")


# Asking more question simulataneoulsy using "or"

if x > y or x < y:
    print("x is not equal to y")
else: 
    print("x is equal to y")


if x != y:
    print("x is not equal to y")
else: 
    print("x is equal to y")

# this is even more efficient than the last one 
