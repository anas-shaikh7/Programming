# Making out own functions
# Scope: variable which only exists in region where the function is defined which is its scope of reach not outside it
def random():
    print("Hello, I am ", end="")# --> you removed the \n (backslash n) 

name = input("who are you? ").capitalize().lstrip()# lstrip strips white space at the left 
random()
print(name)

def bye(someone):
    print("Bye bye", someone+"!")# 

name = input("who are you? ").capitalize().lstrip()# lstrip strips white space at the left 
bye(name)

#or

def bye(name):
    name = input("who r u? ")
    print("Well I am", name)

bye(name) 
