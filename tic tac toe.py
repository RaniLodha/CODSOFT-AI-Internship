import random
# Board representation
board = [' ' for _ in range(9)]
PLAYER = 'X'
AI = 'O'
# Function to print the board
def print_board():
    for i in range(3):
        print(f"{board[i*3]} | {board[i*3+1]} | {board[i*3+2]}")
        if i < 2:
            print("---------")
    print()
# Check for a winner
def check_win(symbol):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(board[a] == board[b] == board[c] == symbol for a, b, c in win_conditions)
# Check if the board is full
def is_full():
    return ' ' not in board
# Minimax function
def minimax(board, depth, is_maximizing):
    if check_win(AI): return 1
    if check_win(PLAYER): return -1
    if is_full(): return 0

    best_score = -float('inf') if is_maximizing else float('inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = AI if is_maximizing else PLAYER
            score = minimax(board, depth + 1, not is_maximizing)
            board[i] = ' '
            best_score = max(score, best_score) if is_maximizing else min(score, best_score)
    return best_score
# AI's move
def ai_move():
    best_score, best_move = -float('inf'), None
    for i in range(9):
        if board[i] == ' ':
            board[i] = AI
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score, best_move = score, i
    board[best_move] = AI
# Player's move
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = PLAYER
                break
            else:
                print("That spot is taken, try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")
# Main game loop
def play_game():
    while True:
        print_board()

        # Player's turn
        player_move()
        if check_win(PLAYER):
            print_board()
            print("Rani wins!")
            break
        if is_full():
            print_board()
            print("It's a draw!")
            break

        # AI's turn
        ai_move()
        if check_win(AI):
            print_board()
            print("AI wins!")
            break
        if is_full():
            print_board()
            print("It's a draw!")
            break
# Run the game
play_game()
