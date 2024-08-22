import milestone_2
from milestone_2 import random_word
word_to_be_guessed = random_word()


class Hangman():
    """
    This class is used to set up and run a version of the classic Hangman game.


    Attributes:
        word (str): the word to be guessed, picked randomly from random_word function imported from milestone_2.py file

        word_guessed (list): a list containing the letters of the word that the user has guessed. Each item of the list will be 
        initiliased to an underscore. The underscore will be overwritten as the player guesses the corresponding letter.

        letters (int): Tracks the number of unique letters in the word that have not been guessed yet.

        num_lives (int): The number of lives the player has remaining (initialised to 5 at the beginning of the game).

        word_list (list): A list of words from which the word to be guessed is randomly selected from.

        list_of_guesses (list): A list of guesses that have already been tried. Initialised to an empty list and appended to as the
        user inputs incorrect guesses.

    Methods:
    -------
    check_guess(guess):
        Converts the guess to lowercase, then checks to see if the guess is in the word variable. If true, guess is appended to the
        word_guessed list and 1 is subtracted from the letters variable, otherwise a message is printed and 1 is subtracted from 
        num_lives.

    ask_for_input():
        Prompts the user to input their guess. It then checks that the value is a single, alphanumerical character. The elif statement
        checks the input against the list_of_guesses, and if True it tells the user they have already guessed that letter. The else
        clause calls the check_guess function and appends the guess to the list_of_guesses list.
    """
        
    def __init__(self, word, num_lives=5):
        self.word = word 
        self.word_guessed = ["_"] * len(self.word)
        self.letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
        """
        Initialises an instance of the Hangman game.

        Parameters
        ----------
        word : str
            The word to be guessed, picked randomly from word_list

        word_guessed : list
            A list of the letters of the word to be guessed.

        letters : int 
            The number of unique letters in the word that have not been guessed yet.

        num_lives : int 
            The number of lives the player has. Initialised to 5 at beggining of the game.

        list_of_guesses : list 
            A list of guesses that have already been tried. Initialised to an empty list.
        """

    
    def check_guess(self, guess):
        """
        Validates and processes the user's guess.

        Converts the guess to lowercase, then checks to see if the guess is in the word, and then updates the game state accordingly.
        - If the guess is correct, it updates the word_guessed list with the guessed letter and decrements the num_letters attribute.
        - If the guess is incorrect, it decrements the num_lives attribute and prints a message.
        
        Parameters
        ----------
        guess : str
            The letter guessed by the player.

        Returns
        -------
        None
            This method does not return anything. It directly modifies the object's state (word_guessed, num_letters, and num_lives).
            """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if guess == self.word[index]:
                    self.word_guessed[index] = letter
                    print(self.word_guessed)
                    self.letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives remaining")
            self.num_lives -= 1

    
    def ask_for_input(self):
        """
        Prompts and validates the user's guess.

        Promps the user to enter their guess, then checks to see if the guess is a single, alphanumeric character.
        - If the input is not valid, it prints a message and prompts the user for another input.
        - If the input has already been entered (appended to the list_of_guesses list), it prints a message and prompts the user for
        another input.
        - If the input is valid and hasn't already been tried, the check_guess method is called and the input is appended to the
        list_of_guesses list.
        
        Returns
        -------
        None
            This method does not return anything. It directly modifies the object's state (list_of_guesses) and passes the guess to the
            check_guess method.
            """
        # while self.num_lives != 0 or self.letters != 0:
        while True:
            guess = input("Please enter your guess: ")
            if len(guess) != 1 and not guess.isalnum():
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            elif self.num_lives == 0:
                print("Sorry, you ran out of lives")
                break
            elif self.letters == 0:
                print("Well done! You guessed the word!")
                break
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


player_1 = Hangman(word_to_be_guessed)

player_1.ask_for_input()