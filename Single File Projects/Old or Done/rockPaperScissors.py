import random

player = input("Rock, Paper, or Scissors? \n")
rand = random.random()

if rand <= .33:
    bot = "Rock"
elif rand <= .66:
    bot = "Paper"
else:
    bot = "Scissors"

print("\n")

if player == "Rock" or player == "rock":
    if bot == "Rock":
        print("It's a tie!")
    elif bot == "Paper":
        print("You lose!")
    elif bot == "Scissors":
        print("You win!")
elif player == "Paper" or player == "paper":
    if bot == "Rock":
        print("You win!")
    elif bot == "Paper":
        print("It's a tie!")
    elif bot == "Scissors":
        print("You lose!")
elif player == "Scissors" or player == "scissors":
    if bot == "Rock":
        print("You lose!")
    elif bot == "Paper":
        print("You win!")
    elif bot == "Scissors":
        print("It's a tie!")

print("")
print("Player chose: " + player)
print("Bot chose: " + bot)

print("\n\nBot's random number:")
print(rand)
