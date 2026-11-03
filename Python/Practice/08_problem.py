class Vector:
    def __init__(self, l):
        self.l = l


    def __len__(self):
        return len(self.l)

    
v1 = Vector([9, 8, 7, 8, 92, 24]) #make list when finding len(length)
print(len(v1))

