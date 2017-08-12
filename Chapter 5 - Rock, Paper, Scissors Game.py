import random

player_choice = input("Rock, Paper, or Scissors?")

def game(player_choice):
    num1 = random.randint(1, 3)
    if num1 == 1:
        print("The computer chose rock.")
        if player_choice == "rock" or player_choice == "Rock":
            print("Stalemate.")
            player_choice = input("Rock, Paper, or Scissors?")
            game(player_choice)
        elif player_choice == "paper" or player_choice == "Paper":
            print("Player wins!")
        elif player_choice == "scissors" or player_choice == "Scissors":
            print("Computer wins!")
    elif num1 == 2:
        print("The computer chose paper.")
        if player_choice == "rock" or player_choice == "Rock":
            print("Computer wins!")
        elif player_choice == "paper" or player_choice == "Paper":
            print("Stalemate.")
            player_choice = input("Rock, Paper, or Scissors?")
            game(player_choice)
        elif player_choice == "scissors" or player_choice == "Scissors":
            print("Player Wins!")
    elif num1 == 3:
        print("The computer chose scissors.")
        if player_choice == "rock" or player_choice == "Rock":
            print("Player wins!")
        elif player_choice == "paper" or player_choice == "Paper":
            print("Computer wins!")
        elif player_choice == "scissors" or player_choice == "Scissors":
            print("Stalemate.")
            player_choice = input("Rock, Paper, or Scissors?")
            game(player_choice)

game(player_choice)

    #play_again = input("Play again?")
    #if play_again == "yes" or play_again == "y" or play_again == "Y" or play_again == "Yes":
    #    choice = True
    #else:
    #    choice = False