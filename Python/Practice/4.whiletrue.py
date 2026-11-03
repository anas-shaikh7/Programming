while True:
    n = int(input("Enter n: "))
    if n < 0:
        continue
    else:
        break

# even simpler would be this: break out if n is greater than 0
while True:
    n = int(input("Enter n: "))
    if n > 0:
        break
for _ in range(n):
    print("meow")
