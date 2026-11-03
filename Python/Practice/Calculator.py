x = input("Enter number: ")
y = input("Enter another number: ")


z = int(x) + int(y)
print("the answer is", z )
# not recommended to use a new variable instead do this 


u = int(input("Enter number: "))
v = int(input("Enter a number: "))
print(u + v)
# so what happens here is that the function input and its argument run first and then this whole new string becomes the argument for the int fucncion


# FLoating point Values: for real numbers with a decimal point



 #round(number[, ndigits]) --> this tells us you can add just one number as there is no *. n gigits tell us the precision or how much should weround upto. If you dont add the precision because its optionlal sas shown by the square brackets(they indicate that whats inside them is optiona), the answer will use to the normal rules of rouncding.
c = float(input("Enter number: "))
d = float(input("Enter a number: "))

print(round(c + d))
print(round(c + d, 3))
#Enter number: 4.592489
#Enter a number: 4.90840348
#10
#9.501
k = float(input("Choose a number: "))
l = float(input("Choose 2nd number: "))

t = k / l
print(f"{t}")
print(f"{t:,}")
m = round(t, 2)
print(m)
#Choose 2nd number: 3
#0.3333333333333333
#0.3333333333333333
#0.33
# another for m = round(t, 2)
print(f"{t:.2f}")




