import random

choices = ["rock","paper","scissors"]
computer_choice = random.choice(choices)


player_choice = input("Input an action, (rock,paper,scissors): ")

if player_choice == computer_choice:
       print("Draw!")

elif player_choice == "rock":
       if computer_choice == "paper":
              print("Paper covers rock, you lose")
       else:
              computer_choice == "scissors"
              print("Rock smashes scissors, you win")

elif player_choice == "paper":
       if computer_choice == "rock":
              print("Paper covers rock, you win")
       else:
              computer_choice == "scissors"
              print("Scissors cuts paper, you lose")

elif player_choice == "scissors":
       if computer_choice == "paper":
              print("Scissors cuts paper, you win")
       else:
              computer_choice == "rock"
              print("Rock smashes scissors, you lose")


