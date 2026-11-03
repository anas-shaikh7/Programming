def main():
    fraction_left = fuel("Fraction Left: ")
    print(fraction_left)

def fuel(fraction):
    while True:
        f = input(fraction).strip()
        try:
            x, y = f.split("/")
            if len(f) >= 3 and int(x) >= 0 and int(y) >=0:
                percentage = (int(x) / int(y)) * 100
                if percentage <= 1:
                    return "E"
                elif 100 >=percentage >= 99:
                    return "F"
                    
                elif percentage > 100:
                    pass
                else: 
                    return f"{int(percentage)}%"
                
        except (ValueError, ZeroDivisionError):
                pass
        


main()
