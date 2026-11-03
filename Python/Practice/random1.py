import random

# number = random.choice(["0", "1", "2", "3", "4", "5", 6, 7, 8, 9, 10])
# print(number)

# coin = random.choice(["heads", "tails"])
# print(coin)




from random import choice
coin = choice(["heads", "tails"])
print(coin)


from random import randint
number = randint(0,100)
print(number)


from random import shuffle

to_learn = ["Python", "Machine Learning", "Deep Learning", "Information Techonology and Systems"]

shuffle(to_learn)

for subject in to_learn:
    print(subject)

