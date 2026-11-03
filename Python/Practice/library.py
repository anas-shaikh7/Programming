import sys
import ML

if len(sys.argv) == 2:
    ML.question1(sys.argv[1])


# sys.argv is a list in Python's sys module that holds the command-line arguments passed to a script when it's run.
# Basic
# sys.argv[0] is always the name (or path) of the script itsel
# sys.argv[1], sys.argv[2], etc. are the arguments that follow, in order, as strings
# Example:
# python
# # script.py
# import sys
# print(sys.argv)
# Running it:
# $ python script.py hello world 123
# ['script.py', 'hello', 'world', '123']


# import sys — gives access to sys.argv, the list of command-line arguments.
# import sayings — imports a module named sayings.py, which must be a file sitting somewhere Python can find it (usually the same folder as this script). It presumably defines a function called hallo.
# if len(sys.argv) == 2: — checks that exactly one command-line argument was passed. Remember, sys.argv[0] is the script name itself, so len(sys.argv) == 2 means "script name + exactly one extra argument."
# sayings.hallo(sys.argv[1]) — if that condition holds, it calls the hallo function from the sayings module, passing in that one argument (probably a name).