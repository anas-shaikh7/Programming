class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __str__(self):
        return f"Vector{self.x}, {self.y}, {self.z}"
    
v1 = Vector(9, 8, 7)
v2 = Vector(6, 5, 4)        
v3 = Vector(3, 2, 1)

print(v1 + v2)
print(v1*v2)


print(v1 + v3)
print(v1*v3)





    