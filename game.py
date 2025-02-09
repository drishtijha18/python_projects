# tik tak tok game 

import os

grid_size = 13
board = [str(i) for i in range(1, 10)]  

def pattern_grid():
    os.system('clear') 
    k = 0
    for i in range(grid_size):
        for j in range(grid_size):
            if (i in [2, 6, 10]) and (j in [2, 6, 10]):
                print(board[k], end=" ")
                k += 1
            elif i in [4, 8] or j in [4, 8]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def is_valid_choice(x):
    return x in [str(i) for i in range(1, 10)] and board[int(x) - 1] not in ["X", "O"]

def update_board(x, turn):
    board[int(x) - 1] = 'X' if turn % 2 == 0 else 'O'

def check_winner():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        a, b, c = condition
        if board[a] == board[b] == board[c]:
            return True
    return False

i = 0
pattern_grid()
print("Welcome to Tic-Tac-Toe, Dristi!")
while i < 9:
    print(f"Player {1 if i % 2 == 0 else 2}'s Turn")
    choice = input("Enter a number (1-9): ")
    if not is_valid_choice(choice):
        print("Invalid choice, please try again!")
        continue
    update_board(choice, i)
    pattern_grid()
    if check_winner():
        print(f"Congratulations! Player {1 if i % 2 == 0 else 2} wins!")
        break
    i += 1
else:
    print("It's a draw!")