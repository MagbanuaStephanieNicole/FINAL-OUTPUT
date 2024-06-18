import random

def get_player_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
        choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    return choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return None  # Tie
    elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
         (player1_choice == 'paper' and player2_choice == 'rock') or \
         (player1_choice == 'scissors' and player2_choice == 'paper'):
        return 'player1'
    else:
        return 'player2'

def main():
    print("Welcome to Rock-Paper-Scissors Game (Best of 3 rounds)!")
    print("Choices are: rock, paper, scissors")
    print("")

    player1_score = 0
    player2_score = 0
    rounds_to_win = 2
    round_number = 1

    # Determine if playing against another player or computer
    opponent_choice = input("Do you want to play against another player (p) or computer (c)? ").strip().lower()

    while player1_score < rounds_to_win and player2_score < rounds_to_win:
        print(f"Round {round_number}:")
        
        if opponent_choice == 'p':
            player1_choice = get_player_choice()
            player2_choice = get_player_choice()
        elif opponent_choice == 'c':
            player1_choice = get_player_choice()
            player2_choice = get_computer_choice()
            print(f"Computer chooses: {player2_choice}")
        else:
            print("Invalid choice! Please enter 'p' for player vs player or 'c' for player vs computer.")
            continue
        
        winner = determine_winner(player1_choice, player2_choice)

        if winner == 'player1':
            print("Player 1 wins this round!\n")
            player1_score += 1
        elif winner == 'player2':
            if opponent_choice == 'p':
                print("Player 2 wins this round!\n")
            else:
                print("Computer wins this round!\n")
            player2_score += 1
        else:
            print("It's a tie for this round!\n")

        round_number += 1

    # Determine overall winner
    if player1_score > player2_score:
        print("Player 1 wins the game!")
    else:
        if opponent_choice == 'p':
            print("Player 2 wins the game!")
        else:
            print("Computer wins the game!")

if __name__ == "__main__":
    main()
