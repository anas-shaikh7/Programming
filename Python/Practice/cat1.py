# print("meow")
# print("meow")
# print("meow")

#task: meow thrice

# i = 3
# while i !=0:
#     print("meow") # if we do tis the while loop will run forever beecause i is always not zero its three
# working of the while loop: 
i = 3
while i !=0:
    print("meow")
    i = i - 1
# the while loop asks a question. when te program first starts, i = 3 so the while loop meows. Now i =  3 - 1 happens. since i !=0 and its 2, so the while lopp runs and a meow is printed. Now again, i = 2 - 1, i !=0 so while loop runs and a meow is printed. again, i = 1-1, NOW i = 0. so the while loop will not print the meow.  


i = 1
while i <= 3:
    print("meow")
    # i = i - 1 You cannot just subtract because the loop with repeat inifinitly. Becuase the result of i - 1 will go to -ve inifiity
    i = 1 + i 

    ## i = 2 + i === i += 1 --> Both are the same methods
    # As programmers, it is a convention to always start from 0
i = 0 
while i <= 2: # or i < 3
    print("meow") 
    i += 1
