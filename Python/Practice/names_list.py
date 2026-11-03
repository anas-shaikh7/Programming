names = []

for _ in range(3): # This just means repeat the intendent code thrice.  
    names.append(input("Was ihr name? ").strip())

for name in sorted(names):
    print(f"Hallo, {name}")
    print(*names)
