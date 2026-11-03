def probability(coin):
    if "Unfair" in coin:
        return "A coin with a vairable chance of landing on either heads or tails, which is not 50%"
    elif "Fair" in coin:
        return "A coin with 50% chance of landing on either heads or tails."
    else:  
        return "error"

coin = input("Which coin: ").capitalize()
print(probability(coin))
    
#process: user gives an input, the python intrprator capitalizes that input and gives it as an argument to the probability function, the probability function analysis this response and then returns the value corressponding to the response.

#########