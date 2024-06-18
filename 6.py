import random

def roll_dice():
    return random.randint(1, 6)  # Simulates rolling a 6-sided dice

def main():
    print("Welcome to the Dice Rolling Simulator Game (Best of 3 rounds)!")
    print("")

    player1_wins = 0
    player2_wins = 0
    rounds_to_win = 2
    round_number = 1

    while player1_wins < rounds_to_win and player2_wins < rounds_to_win:
        print(f"Round {round_number}:")
        
        # Player 1 rolls the dice
        input("Player 1, press Enter to roll the dice.")
        player1_roll = roll_dice()
        print(f"Player 1 rolls: {player1_roll}")

        # Player 2 rolls the dice
        input("Player 2, press Enter to roll the dice.")
        player2_roll = roll_dice()
        print(f"Player 2 rolls: {player2_roll}")

        # Determine round winner
        if player1_roll > player2_roll:
            print("Player 1 wins this round!\n")
            player1_wins += 1
        elif player2_roll > player1_roll:
            print("Player 2 wins this round!\n")
            player2_wins += 1
        else:
            print("It's a tie for this round!\n")

        round_number += 1

    # Determine overall winner
    if player1_wins > player2_wins:
        print("Congrats Player 1 you won the game!")
    else:
        print("Congrats Player 2 you won the game!")

if __name__ == "__main__":
    main()
