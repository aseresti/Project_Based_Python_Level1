import random

class TicTacToe():
    def __init__(self):
        """ The class initially defines an empty board and shows an initial board
        to make it easier for the user to choose one of the cells from the board
        and defines a random first player
        """
        self.empty_board()
        self.initial_board = list(map(str, range(10)))
        self.get_random_first_player()

    def empty_board(self):
        """Defines an empty board
        """
        self.board = [' ']*10 #0th index is ignored.


    def show_empty_board(self):
        """Shows the board with cell numbers for the user to choose from
        """
        print("\n")
        print(self.initial_board[1] + '|' + self.initial_board[2] + '|' + self.initial_board[3])
        print('-'*6)
        print(self.initial_board[4] + '|' + self.initial_board[5] + '|' + self.initial_board[6])
        print('-'*6)
        print(self.initial_board[7] + '|' + self.initial_board[8] + '|' + self.initial_board[9])

    def show_board(self):
        """Shows the game board with or without empty cells
        """
        print("\n")
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print('-'*6)
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print('-'*6)
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])

    def swap_player_turn(self):
        """changes the player turn
        """
        self.player_turn = 'x' if self.player_turn == 'o' else 'o'

    
    def is_board_filled(self):
        """checks if the board has still some empty room

        Returns:
            bool: True if the board is filled.
        """
        return ' ' not in self.board[1:]
    
    def is_cell_filled(self,cell):
        """checks if the selected cell hasn't already been filled.

        Args:
            cell (int): number of the cell index

        Returns:
            bool: True if the cell is already fixed with a player.
        """
        return ' ' not in self.board[cell]
    
    def fix_spot(self,cell):
        """fix the value of the palyer's cell of choice 

        Args:
            cell (int): number of the cell index
        """
        self.board[cell] = self.player_turn

    def has_player_won(self,player):
        """check if the player has won

        Args:
            player (str): whose ever turn it is.

        Returns:
            bool: True if any player meets any of the win combinations
        """
        win_combinations = [
            [1,2,3], [4,5,6], [7,8,9], # rows
            [1,4,7], [2,5,8], [3,6,9], #columns
            [1,5,9], [3,5,7] #diagonals
        ]

        for comb in win_combinations:
                if (
                    self.board[comb[0]] == player and 
                    self.board[comb[1]] == player and 
                    self.board[comb[2]] == player
                ):
                    return True
        
        return False
    
    def get_random_first_player(self):
        """Randomly selects a player
        """
        self.player_turn = random.choice(['x', 'o'])

    
    def play_game(self):
        """play the TicTacToe game by clearing the board and setting a random first player.
        Then, showing the initial board and asking for user input to select a cell. 
        Once the player has selected a cell, it is fixed with them after checking if the
        cell is empty, and then changes the player turn, if no one has not won already
        or the board isn't filled yet.

        Returns:
            func: returns itself if the player choose to play one more time.
        """
        
        print("welcome to the game!")
        print("You can choose any number from the following board to fix your player's spot")
        self.show_empty_board()
        while True:
            print(self.player_turn)

            cell = int(input("input the cell number: "))
            if self.is_cell_filled(cell):
                print('the cell is already fixed.')
                cell = int(input("input another cell number: "))

            self.fix_spot(cell)

            self.show_board()

            if self.has_player_won(self.player_turn):
                print(f'{self.player_turn} has won!')
                play_again = input('press any key to play again or q to quit: ')
                if play_again == 'q':
                    break
                else:
                    self.empty_board()
                    return self.play_game()

            if self.is_board_filled():
                print('The board is filled. No winner.')
                play_again = input('press any key to play again or q to quit: ')
                if play_again == 'q':
                    break
                else:
                    self.empty_board()
                    return self.play_game()

            self.swap_player_turn()

if __name__ == "__main__":
    
    game = TicTacToe()
    game.play_game()