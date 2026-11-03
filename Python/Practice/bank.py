
def main():
    greeting = input("Greeting: " ).lower().strip()
    greet(greeting)


def greet(greeting):
    word = list(greeting) # ---> converts it into list 
    if "hello" in greeting:
        print("$0")

    # elif greeting[0] == "h":
    #     print("$20")
    #     or
    elif word[0] == "h":
        print("$20")

    else:
        print("$100")
main()
