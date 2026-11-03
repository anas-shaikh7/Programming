class Employee:    # Base or Parent Class
    company = "Engro"  # Property
    def show(self):
        print(f"The company of employee is {self.company} and his salary is {self.salary}")



  #class Programmer:
     #company = "Neelum Jhelum Hydropower Plant"
    #def show(self):
  #      print(f"The company of employee is {self.company} and his salary is {self.salary}")

   # def showlanguage(self):
   #     print(f"The name of the employee is {self.name} and the language of the employee is {self.language}")


class Programmer(Employee): # inherites Employee in programmer     #Derived or Child CLass
   company = "Neelum Jhelum Hydropower Plant"               
   def showlanguage(self):   
        print(f"The name of the employee is {self.name} and the language of the employee is {self.language}")


a = Employee()
b = Programmer()
print(a.company, b.company)