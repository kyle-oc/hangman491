from milestone_2 import random_word

random_fruit = random_word()
found_letters = "xxxxxx"
guess = ""

def check_guess(guess):
    guessed_letter = guess.lower()
    if guessed_letter in random_fruit:
        print(f"Good guess! {guessed_letter} is in the word")
    else:
        print(f"Sorry, {guessed_letter} is not in the word. Try again.")


def ask_for_input():
    while True:
        guess = input("Please enter a letter as your guess: ")
        if guess.isalnum and len(guess) == 1:
            check_guess(guess)
        else:
            print("Invalid letter. Please enter a single alphabetical character")


ask_for_input()




