class Employee:
    a = 5

class Programmer(Employee):
    b = 4


class Coder(Programmer):
    c = 3


o = Employee() 
print(o.a) # prints a
#print(o.b) # shows error as employee object does not have the attribute b

o = Programmer()
print(o.a, o.b)
                

o = Coder()
print(o.a, o.b, o.c)