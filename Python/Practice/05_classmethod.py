class Employee:
    a = 1
    @classmethod  # This Decorator will access the class instead  of accessing the instance attribute   as well as the (self)
    def show(cls):
        print(f"The class attributeof a is: {cls.a}")

e = Employee()
e.a = 100

e.show()
