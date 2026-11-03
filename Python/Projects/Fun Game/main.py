'''
"KEY"
Portugal = 100
France = 50
 Portual vs France {Final}
POR 5 FRA 4 = 500
FRA 2 POR 1 = 1000



Portugal won the Euro 2024 = 10
France won the Euro 2024 = 20
'''
import random
computer = random.choice([100, 50])
youstr = input("Enter the team you choose: ")
youDict = {"P": 100, "F": 50}
reverseDict = {100: "Portugal", 50: "France"}
# reverseDict2 = {10:"Portugal won the Euro 2024", 20: "France won the Euro 2024"}

you = youDict[youstr]
print("Welcome to Euros 2024")
print(f"You Chose {reverseDict[you]}\nSystem Chose {reverseDict[computer]}")


if(computer == 100 and you == 50):
      print("Portugal won the Euros 2024")
    
elif(computer == 50 and you == 100):
      print("Portugal won the Euros 2024")
      

elif(computer == 100 and you == 100):
     print("Something went wrong")

else:
     print("Something went wrong")

print("Results")
print("POR 5 - FRA 4")
print("What a night for Cristiano Ronaldo who scored an incredible banger at an age of 39, Messi missed Ronaldo didnt")




            





