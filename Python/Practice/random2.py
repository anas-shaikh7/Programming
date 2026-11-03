import random
# from random import shuffle
from random import choices #To use this do not use random.choices() but do it like this biased_coin = choices(coin, weights=weight, k=1)


# selecting_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# shuffle(selecting_numbers)
# for number in selecting_numbers:
#     print(number)

weight =[80, 20]
coin = ["Heads", "Tails"]
biased_coin = choices(coin, weights=weight, k=1)
print(*biased_coin)