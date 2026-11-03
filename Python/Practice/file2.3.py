y = input("Whats your name? ").strip().title() # cleanest method 
# y = y.title()
print("My name is " + y)
# you need to understand how this works. the strip method first removes the unwanted white space on the sides of words and returns the sentence with no white space. This resulting string now goes to the title method which capitalizes the first letter of every word and returns the final value.


first, second, third = y.split(" ")
print(f"My name is", third) # this gives Shaikh for anas ahmed shaikh 


 # this single white space indicates that we want to split after the first word and second word. the single string y is divided into three sub strings
# In Python, a string is a sequence of Unicode characters used to represent textual data. You can think of it as a collection of letters, numbers, symbols, and spaces wrapped in quotes.