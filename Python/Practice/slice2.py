import sys


if len(sys.argv) < 4:
    sys.exit("KAKI! Look at the condition properly!")
for arg in sys.argv[1:]:
    print(f"Hello! I am", arg)