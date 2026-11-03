#Can we use a string inside a string?
name = input("Whats your name mate? ")
# remember the strings <""> and <''> are the same thing. in python 
print("hello 'mate'")
print('hello "mate"')
print("hello \"anas\"")
# \ this baskslash character means scape and it lets us remove the quotations 

print(f"hello I am {name}") # a newfeature in ython allows us to do this as well


# Built into strings is a datatype which allows 


# Building things professioanlly

y = float(input("Choose a number: "))
x = float(input("Choose 2nd number: "))

z = x + y
print(f"{z}")
print(f"{z:,}")

#choose a number: 100000           
#Choose 2nd number: 100000
#200000.0
#200,000.0   ---> This is how u build professionally to ensure the reader understands the number. not just random numbers so reader keep on counting forever.