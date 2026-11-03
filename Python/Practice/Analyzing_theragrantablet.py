contents_of_theragran = input("Which nutrient's amount are you looking for in theragran? ").title()


match contents_of_theragran:
    case "Vitamin A":
        print("1200 mcg")
    case "Beta Carotene":
        print("600 mcg")
    case "Vitamin D":
        print("10 mcg")
    case "Vitamin E":
        print("20100 mcg")
    case "Vitamin C":
        print("90mg")
    case "Vitamin B1" | "Vitamin B6":
        print("3mg")
    case "Vitamin B2":
        print("3.4mg")
    case "Vitamin B12":
        print("9mcg")
    case "Pantothenic Acid":
        print("10mg")
    case "Folic Acid":
        print("0.4mg")
    case "Biotin":
        print("30mcg")
    case "Niacin":
        print("20mg")
    case "Iron":
        print("27mg")
    case "Calcium":
        print("40mg")
    case "Phosphorus":
        print("31mg")
    case "Iodine":
        print("150mcg")
    case "Magnesium":
        print("100mg")
    case "Copper":
        print("2mg")
    case "Zinc":
        print("15mg")
    case "Manganese":
        print("5mg")
    case "Selenium":
        print("10mcg")
    case "Molybdenum" | "Chromium":
        print("15mcg")
    case "Potassium" | "Chloride":
        print("7.5mg")
    case _: 
        print("Not found")


#Calculating moles of contents in theragran

Moles = float(input("Enter mass: ")) / float(input("Enter Mr: "))
# print(round(f"{Moles}mol", 5))
print(f"{round(Moles, 5)}mol" )


#print(Moles + "mol") -- > this is wrong because python cannot add a float point number and a string