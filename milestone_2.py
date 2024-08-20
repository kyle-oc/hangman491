def random_word():
    import random
    word_list = ["bananas", "blueberries", "oranges", "mangos", "watermelon"]
    print(word_list)
    random_word = random.choice(word_list)
    print(random_word)
    return random_word


# if __name__ == "__main__":
# guess = "guess"
# while len(guess) != 1 and guess.isalnum:
#     print("That's not a valid entry")
#     guess = str(input("Please enter your guess: "))
# else:
#     print(guess)

