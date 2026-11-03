# lets say I want to remove s
a = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10" # a is like a container containing all these values(data)
# lets say i want to remove 6 and replace it with 1000, and I want to remove 9 entirely. I will do this
k = a.replace("6", "1000").replace("9", "")
print(k)
# output --> 1, 2, 3, 4, 5, 1000, 7, 8, , 10.

# REMEMBER return = output value + stop function immediately. the subsequent code is never run just whta was before reuturn is run                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 