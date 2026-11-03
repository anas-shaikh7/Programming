# Comparing the probabilities of fair and un fair coins and concluding -- using lecture 1 and 2

# discussing possible biased coins
PH = float(input("Enter P(H): "))
PT = float(input("Enter P(T): "))
Total = PH + PT


# if Total > 1 or Total < 0 or Total < 1:
# if Total > 1 or Total < 1:
if Total != 1: # Shortest possible method 
    print("Impossible ")
else: 
    print("Correct")


# match Total: 
#    case > 1 | < 0 | < 1: 
#         print("Incorrect")
# In a match-case statement (Python 3.10+), you cannot write conditions like Total > 1 directly inside case.

# case is for pattern matching, not for normal boolean conditions.
# Also, | in case is not "OR" for conditions — it’s used to match multiple patterns, like:




