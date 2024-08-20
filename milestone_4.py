import milestone_2
from milestone_2 import random_word
bastard = random_word()


class Hangman():
    def __init__(self, word, num_lives=5):
        self.word = word # the word to be guessed, picked randomly from word_list
        self.word_guessed = ["_"] * len(self.word) # a list of the letters of the word to be guessed. the list will be the length of the word,
        # and each item will be initiliased to a '_'. The '_' will be overwritten as the player guesses the corresponding letter.
        self.letters = len(set(self.word)) # int. Tracks the number of unique letters in the word that have not been guessed yet.
        self.num_lives = num_lives # int. The number of lives the player has at the beginning of the game. 
        # self.word_list = word_list # list. A list of words from which the word to be guessed is randomly selected from.
        self.list_of_guesses = [] # list. A list of guesses that have already been tried. Initialised to an empty list.

    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if guess == self.word[index]:
                    self.word_guessed[index] = letter
                    print(self.word_guessed)
        else:
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives remaining")
            self.letters -= 1
            self.num_lives -= 1

    
    def ask_for_input(self):
        while self.num_lives != 0 or self.letters != 0:
            guess = input("Please enter your guess: ")
            if len(guess) != 1 and not guess.isalnum():
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                

jizzum = Hangman(bastard)

jizzum.ask_for_input()