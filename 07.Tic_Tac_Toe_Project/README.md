# Tic Tac Toe Game

This is a simple implementation of the classic Tic Tac Toe game in Python. The game allows two players to take turns marking cells in a 3x3 grid, aiming to achieve a winning pattern of their marker ('x' or 'o').

## How to Play

To start the game, run the script. Upon starting, the game will display an empty board with cell numbers for reference. Players take turns entering the number of the cell they want to mark.

## Game Rules

- The game randomly selects a starting player.
- Players take turns marking empty cells with their symbol ('x' or 'o').
- The game ends when one player achieves a winning pattern or when all cells are filled.
- Players can choose to play again after the game ends.

## Class Structure

The code is organized into a class called `TicTacToe`, which encapsulates the game's logic. Here's an overview of the class methods:

- `__init__()`: Initializes the game by creating an empty board and selecting a random starting player.
- `empty_board()`: Defines an empty game board.
- `show_empty_board()`: Displays the initial board with cell numbers for reference.
- `show_board()`: Displays the current state of the game board.
- `swap_player_turn()`: Switches the turn between players.
- `is_board_filled()`: Checks if the game board is completely filled.
- `is_cell_filled()`: Checks if a specific cell is already filled.
- `fix_spot()`: Marks a chosen cell with the current player's symbol.
- `has_player_won()`: Checks if the current player has achieved a winning pattern.
- `get_random_first_player()`: Randomly selects the starting player.
- `play_game()`: Manages the game flow, including player turns, cell selection, win detection, and replay option.

## How to Run

To play the game, simply execute the script. Follow the prompts to select cells and continue playing until there's a winner or the board is filled.

Enjoy playing Tic Tac Toe!
