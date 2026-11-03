class Employee:    # Base or Parent Class
    company = "Engro"  # Property
    name = "Default Khalid"                  
    def show(self):
        print(f"The name of the employee is {self.name} and his company is {self.company}")


class Coder:
    language = "Python"
    def printlanguage(self):
        print(f"The language that every employee working 9 to 5 at this company be familiar with must be {self.language}")






class Programmer(Employee, Coder): # inherites Employee in programmer     #Derived or Child CLass
   company = "Neelum Jhelum Hydropower Plant"               
   def showlanguage(self):   
        print(f"The name of the employee is {self.name} and the language of the employee is {self.language}")


a = Employee()
b = Programmer()
b.show()
b.printlanguage()
b.showlanguage()
