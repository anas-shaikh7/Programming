names = []

for _ in range(3):
    name = input("What's your name? ")
    names.append(name)

print(*names)












# for _ in range(3): loops 3 times, using _ as a throwaway variable name since the loop index isn't needed inside the loop body. It's equivalent to running the indented code block 3 times in a row.

