def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum() and s[:2].isalpha():# CS50
        for c in s: 
            if s.isalpha():
                return True
            elif c.isdigit(): 
                i = s.index(c)
                if s[i:].isdigit() and c != "0":
                    return True
                else:
                    return False
            
 


main()