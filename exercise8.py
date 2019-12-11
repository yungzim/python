

while True:
    player1 = input("Player 1: Enter Rock, Paper, Scissors: ").lower()
    player2 = input("Player 2: Enter Rock, Paper, Scissors: ").lower()

    if player1 == player2 and player2 == player1:
        print(f"both players chose {player2}, you have to play again")
    elif player1 == "rock" and player2 == "scissors":
        print(f"rock beats scissors. Player 1 wins")
        break
    elif player2 == "rock" and player1 == "scissors":
        print(f"rock beats scissors. Player 2 wins")
        break

    elif player1 == "scissors" and player2 == "paper":
        print(f"scissors beats paper. Player 1 wins")
        break
    elif player2 == "scissors" and player1 == "paper":
        print(f"scissors beats paper. Player 2 wins")
        break

    elif player1 == "paper" and player2 == "rock":
        print(f"paper beats rock. Player 1 wins")
        break
    elif player2 == "paper" and player1 == "rock":
        print(f"paper beats rock. Player 2 wins")
        break
    else:
        print("Invalid input")


