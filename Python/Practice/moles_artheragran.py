#plan --> calculate moles = g/mr
# conversion mcg --> g, mg --> g
# store mr values

contents_of_theragran = input("Which nutirent's mass do you want                                                                                                                                                                                                                                                                                                                                                ? ").title()


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


def main():
    nutrient = input("Amount of which nutrient: ").title().strip()
    amount(nutrient)
   

def amount(nutrient):
    match nutrient:
        case "Vitamin A":
            m = "1200mcg"
            MR = 286
        case "Beta Carotene":
            m = "600mcg"
            MR = 536
        case "Vitamin D":
            m = "10mcg"
            MR = 384

        case "Vitamin E":
            m = "20100mcg"
            MR = 430

        case "Vitamin C":
            m = "90mg"
            MR = 176
            
        case "Vitamin B1":
            m = "3mg"
            MR = 337
        case  "Vitamin B6":
            m = "3mg"
            MR = 169           
        case "Vitamin B2":
            m = "3.4mg"
            MR = 376
        case "Vitamin B12":
            m = "9mcg"
            MR = 1355
        case "Pantothenic Acid":
            m = "10mg"
            MR = 219
            
        case "Folic Acid":
            m = "0.4mg"
            MR = 441
        case "Biotin":
            m = "30mcg"
            MR = 244
        case "Niacin":
            m = "20mg"
            MR = 123
      
        case "Iron":
            m = "27mg"
            MR = 56
            print("27mg")
        case "Calcium":
            m = "40mg"
            MR = 40
        case "Phosphorus":
            m = "31mg"
            MR = 31
         
        case "Iodine":
            m = "150mcg"
            MR = 127
            
        case "Magnesium":
            m = "100mg"
            MR = 24
        case "Copper":
            m = "2mg"
            MR = 63.5
           
        case "Zinc":
            m = "15mg"
            MR = 65
  
        case "Manganese":
            m = "5mg"
            MR = 55
        
        case "Selenium":
            m = "10mcg"
            MR = 79
        
        case "Molybdenum": 
            m = "15mcg"
            MR = 96
        case "Chromium":
            m = "15mcg"
            MR = 52           
        case "Potassium":
            m = "7.5mcg"
            MR = 39
        case "Chloride":
            m ="7.5mg"
            MR = 35.5
        case _: 
            print("Not found")
    if "mcg" in m:
        # m = m.replace("mcg", "")
        # m  = float(m)
        # m =  m * pow(10, -6)

        m = float(m.replace("mcg", "")) * pow(10, -6)       
    elif "mg" in m:
        # m = m.replace("mg", "")
        # m = float(m)
        # m = m * pow(10, -3)
        m = float(m.replace("mg", "")) * pow(10, -3)
        # return m* pow(10, -6) --> this return is worng because it stops the function immediately after converting th value, so subsequent code never runs,
    # moles = float(m*pow(10, -2)) / float(MR)
    moles = m / float(MR)
    print(f"{round(moles, 20)}mol" )


main()

#   1. match-case concept
# match value: → Python looks at the value stored inside a variable
# case "something": → checks if the value equals that string
# _ → wildcard (matches anything) → like else
# Example:
# match nutrient:
#     case "Vitamin A":
#         print("1200 mcg")
#     case _:
#         print("Not found")
# 🧠 2. What _ means
# _ means “I don’t care what the value is”
# It is used as a default case
# case _:

# 👉 same idea as:

# else:
# 🧠 3. OR pattern in match-case
# case "Vitamin B1" | "Vitamin B6":

# 👉 means:

# match Vitamin B1 OR Vitamin B6

# This is called an OR pattern

# 🧠 4. Variables inside cases (m, MR)
# case "Vitamin A":
#     m = 1200
#     MR = 286
# What this means in CS terms:
# m and MR are normal local variables
# They are created only when that case runs
# They are not special or linked to match-case

# 👉 This is called block scope (local scope)

# 🧠 5. Variable scope (important concept)
# Variables inside a block (like a case) are local
# They exist only during execution of that block

# 👉 Concept: local scope

# 🧠 6. = vs ==
# ✔ =

# 👉 assignment (store value)

# m = 1200
# ✔ ==

# 👉 comparison (check equality)

# m == 1200
# 🧠 7. Function calling vs comparison mistake
# amount(nutrient, nutrient) == nutrient
# Problems:
# == does NOT call functions
# function call is amount(...)

# 👉 Correct:

# amount(nutrient)