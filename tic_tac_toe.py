import random
from rich.console import Console

def print_board(board):
    console = Console()
    console.print("Tic-Tac-Toe")
    for i in range(3):
        row = " | ".join(board[i])
        console.print(row)
        if i < 2:
            console.print("---------")

def check_win(board, symbol):
    # Check rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2-i] == symbol for i in range(3)):
        return True
    return False

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def computer_move(board, computer_symbol, player_symbol):
    empty_cells = get_empty_cells(board)
    if len(empty_cells) == 9:
        # If it's the computer's first move, choose a random cell
        return random.choice(empty_cells)
    
    # Check if computer can win in next move
    for cell in empty_cells:
        board[cell[0]][cell[1]] = computer_symbol
        if check_win(board, computer_symbol):
            return cell
        board[cell[0]][cell[1]] = " "
    
    # Check if player can win in next move and block
    for cell in empty_cells:
        board[cell[0]][cell[1]] = player_symbol
        if check_win(board, player_symbol):
            board[cell[0]][cell[1]] = computer_symbol
            return cell
        board[cell[0]][cell[1]] = " "
    
    # If no winning move, choose random empty cell
    return random.choice(empty_cells)

def main():
    console = Console()
    console.print("Welcome to Tic-Tac-Toe!", style="bold green")
    user_choice = console.input("Would you like to go [bold]first[/bold] or [bold]second[/bold]? ").lower()
    player_symbol = "X"
    computer_symbol = "O"
    if user_choice == "second":
        player_symbol, computer_symbol = computer_symbol, player_symbol
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    while True:
        # Player's move
        if player_symbol == "X":
            print_board(board)
            row = int(console.input("Enter row (1, 2, or 3): ")) - 1
            col = int(console.input("Enter column (1, 2, or 3): ")) - 1
            if board[row][col] == " ":
                board[row][col] = player_symbol
            else:
                console.print("That cell is already occupied. Try again.", style="bold red")
                continue
        else:
            row, col = computer_move(board, computer_symbol, player_symbol)
            board[row][col] = player_symbol
        
        if check_win(board, player_symbol):
            print_board(board)
            console.print("Congratulations! You win!", style="bold green")
            break
        elif " " not in [cell for row in board for cell in row]:
            print_board(board)
            console.print("It's a tie!", style="bold yellow")
            break
        
        # Computer's move
        if player_symbol == "O":
            print_board(board)
            row = int(console.input("Enter row (1, 2, or 3): ")) - 1
            col = int(console.input("Enter column (1, 2, or 3): ")) - 1
            if board[row][col] == " ":
                board[row][col] = computer_symbol
            else:
                console.print("That cell is already occupied. Try again.", style="bold red")
                continue
        else:
            row, col = computer_move(board, computer_symbol, player_symbol)
            board[row][col] = computer_symbol
        
        print_board(board)
        if check_win(board, computer_symbol):
            console.print("Sorry, you lose!", style="bold red")
            break
        elif " " not in [cell for row in board for cell in row]:
            console.print("It's a tie!", style="bold yellow")
            break

if __name__ == "__main__":
    main()