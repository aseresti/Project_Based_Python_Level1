import random
from typing import List, Dict


class rock_paper_scissor():
    """This class implements the rock paper scissors game.
    """

    def __init__(self) -> None:
        self.choices: List[str] = ['rock', 'paper', 'scissor']

    def get_computer_choice(self) -> str:
        """the function gets the computer choices and returns it as str

        :return: computer random choice from rock, paper, scissor
        :rtype: str
        """
        return random.choice(self.choices)
    
    def get_user_choice(self) -> str:
        """the function gets user choices and returns it as a str

        :return: the input user choice
        :rtype: str
        """
        user_choice = input(f'Enter your choice:({[ch for ch in self.choices]})')
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        else:
            print("Input is not valid")
        return self.get_user_choice()
    
    def select_winner(self, user_choice:str, computer_choice:str) -> str:
        """the function defines the loss or win situation

        :param user_choice: the user input
        :type user_choice: str
        :param computer_choice: computer random choice
        :type computer_choice: str
        :return: win/loss situation
        :rtype: str
        """
        win_situation: Dict[str] = {'rock':'scissor','scissor':'paper','paper':'rock'}
        if computer_choice == win_situation[user_choice]:
            return "Congratulations! You won"
        elif user_choice == computer_choice:
            return "It's a tie"
        else:
            return "You Lost"
        
    def play_again(self):
        """The function gets the user choice on playing more of the game

        :return: exit or play game function
        :rtype: function
        """
        play_again = input('press any key to play again or q to exit')
        if play_again == 'q':
            return None
        else:
            return self.play_game()

    
    def play_game(self):
        """The main function of the game

        :return: play again func to ask user for their input
        :rtype: function
        """
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print(f"computer choice is: {computer_choice}")
        winner = self.select_winner(user_choice, computer_choice)
        print(winner)
        return self.play_again()
    
    
if __name__ == "__main__":
    rock_paper_scissor().play_game()