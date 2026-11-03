class Number:
    def __init__(self, n): # Dunder method
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    

n = Number(1)
m = Number(99)

print(n + m)