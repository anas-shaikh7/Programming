class Employee:
    
   @property
   def name(self):
      return f"{self.fname} {self.lname}"
   
   @name.setter
   def name(self, value):
      self.fname = value.split(" ")[1] # splits them according to the value given
      self.lname = value.split(" ")[2]
e = Employee()
e.name = " Anas Shaikh"
print(e.fname, e.lname)
  # f.name  = first name # l.name = last name 