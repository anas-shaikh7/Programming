def main():

    y = input("Input: ")

    vowels =["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    # output = ''
    for vowel in vowels:
        if vowel in y:
            y = y.replace(vowel, "") # The for loop repeats for all the vowel in vowels. The variable gets changed each time the loop runs. After the iterations are completed the final value of y gets printed outside the loop. Keeping the print func inside the loop will print the changed value untill all the values are changed. 
    print(y)
main()