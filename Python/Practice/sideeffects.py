function = "quadratic"# global variable

def main(): 
    func = input("which function's identity do you want? A function which contains ").capitalize()
    global function # made global variable modifiable
    if  "X^2" in func:
        polynomial(function)
    elif "X^3" in func:
        function = "cubic"
        polynomial(function)
    elif  "X^4" in func:
        function = "quartic"
        polynomial(function)
    else:
        function = "error"



def polynomial(some):
    print("This function is called", some, "function " )


main()

    
    
         