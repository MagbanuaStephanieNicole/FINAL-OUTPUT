def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def main():
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 will be X and Player 2 will be O.")
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")

    current_player = 1
    board = [[' ']*3 for _ in range(3)]
    game_over = False

    while not game_over:
        print_board(board)

        if current_player == 1:
            print(f"{player1}'s turn (X)")
        else:
            print(f"{player2}'s turn (O)")

        row = int(input("Enter row number (0, 1, 2): "))
        col = int(input("Enter column number (0, 1, 2): "))

        if board[row][col] == ' ':
            if current_player == 1:
                board[row][col] = 'X'
                if check_winner(board, 'X'):
                    print_board(board)
                    print(f"Congratulations! {player1} wins!")
                    game_over = True
                elif is_board_full(board):
                    print_board(board)
                    print("It's a draw!")
                    game_over = True
                current_player = 2
            else:
                board[row][col] = 'O'
                if check_winner(board, 'O'):
                    print_board(board)
                    print(f"Congratulations! {player2} wins!")
                    game_over = True
                elif is_board_full(board):
                    print_board(board)
                    print("It's a draw!")
                    game_over = True
                current_player = 1
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    main()
