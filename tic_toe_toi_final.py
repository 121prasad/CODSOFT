import random

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 13)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_player_move(board, player):
    while True:
        try:
            if player == 'user':
                move = int(input(f"Player X, enter your move (1-9): "))
            else:
                move = random.randint(1, 9)

            if 1 <= move <= 9:
                row, col = divmod(move - 1, 3)
                if board[row][col] == ' ':
                    return row, col
                else:
                    print("Cell already occupied. Try again.")
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['user', 'AI']
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)

        # Get player move
        row, col = get_player_move(board, players[current_player])
        board[row][col] = 'X' if players[current_player] == 'user' else 'O'

        # Check if the player wins
        if check_winner(board, 'X'):
            print_board(board)
            print("Player X wins!")
            break

        # Check if the AI wins
        if check_winner(board, 'O'):
            print_board(board)
            print("Player O (AI) wins!")
            break

        # Check if the board is full (draw)
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch to the next player
        current_player = 1 - current_player

if __name__ == "__main__":
    main()
