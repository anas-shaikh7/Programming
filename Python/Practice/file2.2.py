name = input("whats your name?")


name = name.strip() # this is called a method 
# there a  lot of functions in python adn their functionality can be accessied by using thus 
name = name.capitalize()

print(f"hello, {name}" ) # but this doesent capitallizes the first letter of all the words le this Anas Ahmed but it just did this Anas

# since we want the 1st letter of both words to be capitallized we will do this 

# Another method

x = input(" todays topic? ")
x = x.capitalize().strip()

print(f" the topic for today is {x}")

# One more method the best one -- short
z = input("say something").capitalize().strip() # remember capitallize sjust opposes what you do the first letter of a word
print(z)

