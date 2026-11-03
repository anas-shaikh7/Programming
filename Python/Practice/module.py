def myFunc():
    print("Hello boi")
    
if __name__ == "__main__": # this is placed when you dont want to present the name of the file.
    #if this code is directly executed by running the file its present in
    print("We are directly running this code")
    myFunc()
    print(__name__) #this will print the name of the main file when this code is run in module and will print module when it is run in main