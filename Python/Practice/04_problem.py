class Employee:
     salary = 100
     increment = 20


     @property
     def salaryafterincrement(self):
          return (self.salary + self.salary * (self.increment/100))
     
     @salaryafterincrement.setter
     def salaryafterincrement(self, salary):
          self.increment = (salary/salaryafterincrment)*100
          

e = Employee()
#print(e.salaryafterinccrement)

salaryafterincrment = 120
print(e.increment)