"""
OOP implementation of a password generator
"""
import random
import string
from abc import ABC, abstractmethod
from typing import Optional, List

import nltk

nltk.download('words')


class PasswordGenerator(ABC):
    """
    Base class for password generation
    """
    @abstractmethod
    def generate(self) -> str:
        """Override this method to generate password

        :rtype: str
        """
        pass


class RandomPasswordGenerator(PasswordGenerator):
    """
    class to generate random password
    """
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self) -> str:
        """Main method of generating the password

        :return: Password
        :rtype: str
        """
        return ''.join(random.choice(self.characters) for _ in range(self.length))


class MemorablePasswordGenerator(PasswordGenerator):
    """
    class to generate memorable random password
    """
    def __init__(
        self,
        no_of_words: int = 4,
        seperator: str = "-",
        capitalize: bool = False,
        Vocabulary: Optional[List[str]] = None
        ):

        self.no_of_words: int = no_of_words
        self.seperator: str = seperator
        self.capitalize: bool = capitalize
        self.Vocabulary: List[str] = Vocabulary

        if Vocabulary is None:
            self.Vocabulary = nltk.corpus.words.words()
        
    def generate(self) -> str:
        """
        Generates a password from a list pf Vocabularies
        """
        password_words = [random.choice(self.Vocabulary) for _ in range(self.no_of_words)]

        if self.capitalize:
            password_words = [word.upper() if random.choice([True,False]) else word.lower() for word in password_words]
        
        return self.seperator.join(password_words)


class PinCodeGenerator(PasswordGenerator):
    """
    class to generate pin code
    """
    def __init__(self, length: int = 4):
        self.length = length

    def generate(self):
        """
        generates a pin code with given length
        """
        return ''.join(random.choice(string.digits) for _ in range(self.length))


def main():
    print('--- test random password generator. The password is:')
    RandPass = RandomPasswordGenerator(16, True, True)
    print(RandPass.generate())
    print('--- test memorable password generator. The password is:')
    password = MemorablePasswordGenerator(no_of_words = 5, seperator = "+", capitalize = True)
    print(password.generate())
    print('--- test pin code generator. The password is:')
    pincode = PinCodeGenerator(length=6)
    print(pincode.generate())


if __name__ == "__main__":
    main()