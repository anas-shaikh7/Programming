meals = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    Total = 0
    while True: 
        try:
            meal = input("Item: ").title().strip()
            if meal in meals:
                x = meals[meal] 
                Total = x + Total 
                print(f"Total: ${Total:.2f}")
        except EOFError:
            break  
main()