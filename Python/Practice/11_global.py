def fun():
    global a
    a = 4  # a is local which will run when a function is applied
    print(a)


a = 30
fun()    # this is global which can run both inside a function and outside it. this 30 is not the property of the function
print(a)           #it will run anways until you change it will global
