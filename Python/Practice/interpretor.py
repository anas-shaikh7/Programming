
def main():
    expression = input("Expression: ").strip()
    expression = calculation(expression)
    print(expression)

def calculation(process):
    x, y, z = process.split(" ")
    a = int(x)
    b = int(z)
    if   y == "+" :
        return float(a + b)
    elif y == "-":
        return float(a - b)
    elif y == "*":
        return float(a * b)
    elif y == "/" and b != 0:
        return float(a / b)
    else:
        return "INVALID"


main()
