import random

user_name = input("Enter Name: ")
user_wins = 0
system_wins = 0
game = ["rock", "paper", "scissors"]
for _ in range(0, 3):
    while True:
        user_attempt = input("Rock, Paper or Scissors: ").lower()
        system_attempt = random.choice(game)
        if user_attempt not in game:
            continue
        elif system_attempt == user_attempt:
            print(f"Computer: {system_attempt}")
            continue
        elif system_attempt == "scissors" and user_attempt == "rock":
            print(f"Computer: {system_attempt}")
            user_wins += 1
            print(f" {user_name} points = {user_wins}")
            print(f"Computer points = {system_wins}")
            break
        elif system_attempt == "paper" and user_attempt == "scissors":
            print(f"Computer: {system_attempt}")
            user_wins += 1
            print(f" {user_name} points = {user_wins}")
            print(f"Computer points = {system_wins}")
            break
        elif system_attempt == "rock" and user_attempt == "paper":
            print(f"Computer: {system_attempt}")
            user_wins += 1
            print(f" {user_name} points = {user_wins}")
            print(f"Computer points = {system_wins}")
            break
        else:
            print(f"Computer: {system_attempt}")
            system_wins += 1
            print(f"Computer points = {system_wins}")
            print(f" {user_name} points = {user_wins}")
            break
            

if user_wins > system_wins:
    print(f"{user_name} Wins!")
else:
    print("Computer Wins!")