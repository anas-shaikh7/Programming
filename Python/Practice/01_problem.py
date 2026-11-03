class TwoDVector:
    def __init__(self, n, x):
        self.n = n
        self.x = x

    def show(self):
        print(f"The vector is {self.n}n + {self.x}x")


class ThreeDVector(TwoDVector): # inherits 2d into 3d vector
    def __init__(self, n, x, t):
        super().__init__(n, x) # places the values of twodvecctor in three d vector as well
        self.t = t


    def show(self):
        print(f"The vector is {self.n}n + {self.x}x + {self.t}t") #self.t  indicates the values given eg 10, 9 and 8 for t


a = TwoDVector(10, 9)
a.show()
b = ThreeDVector(10, 9, 8)
b.show()

        