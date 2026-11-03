from goodbye4 import tchuss 

def main():
    test_tchuss_default()
    test_tchuss_argument()


def test_tchuss_default():
    assert tchuss() == "Auf Wiedersehen, Welt"

def test_tchuss_argument():
    assert tchuss("cat") == "Auf Wiedersehen, cat"
if __name__ == "__main__":
    main()




    # This does not work because tchuss does not return anything like the square funtion did earlier, and printing is a side effect like it pops up when the program runs, but it does not store your data like a variable does.
    # It is advised not to have side effect if you want your code to be testable.
    # So now we return it 
    #  Assert is used for argments into function return values
    # To make this even better, and to identify bugs more clearly. we create seperate functions to test the default value and then the arguments that were passed. 