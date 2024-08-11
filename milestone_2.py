import random

word_list = ["bananas", "blueberries", "oranges", "mangos", "watermelon"]
print(word_list)

random_word = random.choice(word_list)
print(random_word)


# guess = "guess"
# while len(guess) != 1 and guess.isalnum:
#     print("That's not a valid entry")
#     guess = str(input("Please enter your guess: "))
# else:
#     print(guess)

user_guess = input("Please enter your guess: ")
if len(user_guess) == 1 and user_guess.isalnum:
    print("Good guess!")
else:
    print("Oops! That is not a valid input")

