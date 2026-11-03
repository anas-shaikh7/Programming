from functools import reduce
#MAP
l = [5, 6, 7, 8, 9, 10]

square = lambda x: x*x

sqlist = map(square, l)
print(list(sqlist))

#FILTER
def even(n):
    if (n%2 == 0):
        return True
    return False 

onlyevenno = filter(even, l)
print(list(onlyevenno))

#REDUCE 
#it needs to be imported from functools

def sum(a, b):
    return a + b

mul = lambda x,t: x*t
print(reduce(sum, l))
print(reduce(mul, l))

