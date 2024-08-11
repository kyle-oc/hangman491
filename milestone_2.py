import random

word_list = ["bananas", "blueberries", "oranges", "mangos", "watermelon"]
print(word_list)

word = random.choice(word_list)
print(word)


# guess = "anus"
# while len(guess) != 1 and guess.isalnum:
#     print("That's not a valid entry")
#     guess = str(input("Please enter your guess: "))
# else:
#     print(guess)

guess = input("Please enter your guess: ")
if len(guess) == 1 and guess.isalnum:
    print("Good guess, dingus!")
else:
    print("Oops! That is not a valid input")



