# ANOTHHER One
print("meow") #meowmeowmeow
print("meow\n" * 3) # \n instroduces a line break after meow. But a line break after thired(last) meow aswell
# output: 
# meow
# meow
# meow
#_______________________________________________________________________________________
# this blank space gets introduced because by defaullt the parameter is end="\n"
print("meow\n" * 3, end="") 
# output: 
# meow
# meow
# meow
# no line breaks here so no extra spaces
print("doggi\n" "doggi\n"  "doggi\n", end="")
print("doggi\n" "doggi\n"  "doggi") # if you add a line break after doggi you wont need to place end="" 