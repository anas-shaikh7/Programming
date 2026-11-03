class Animals:
    pass

class Pets(Animals):
    pass


class Dog(Pets):
     
     @staticmethod
     def bark():
        print("Bhau Bhau!!!!!")

d = Dog()
d.bark()