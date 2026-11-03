def main():
    n = int(input("Enter n: "))
    meow(n)

def meow(n):
    while True:
        print("meow\n" * n, end="")
        if n > 0:
            break

main()


def main():
    number = get_number(number)
    meow(number)

def get_number():
    while True:
        number = int(input("Enter n: "))
        if number > 0:
            break
    return number
def meow(n):
    for _ in range(n):
        print("meow")