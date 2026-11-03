class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 5

class Programmer(Employee):
    def __init__(self):
        super().__init__() # prints the parent object as well
        print("Constructor of Programmer")
    b = 4


class Coder(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Coder")
    
    c = 3


#o = Employee() 
#print(o.a) # prints a
#print(o.b) # shows error as employee object does not have the attribute b

#o = Programmer()
#print(o.a, o.b)
                

o = Coder()
print(o.a, o.b, o.c)