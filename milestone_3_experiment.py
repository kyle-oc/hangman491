# while True:
#     guess = input("Please enter a letter as your guess: ")
#     if guess.isalnum and len(guess) == 1:
#         break
#     else:
#         print("Invalid letter. Please enter a single alphabetical character")


from milestone_2 import random_word

random_fruit = "banana" # random_word() TODO change back to random_word function
found_letters = "xxxxxx"
guess = ""

while random_fruit != guess:
    guess = input("Please enter a letter as your guess: ")
    if guess in random_fruit:
        for index, char in enumerate(random_fruit):
            if char == guess:
                print(index, char)
                found_letters[index] += char # TODO: Make this shit work! Need to work out how to index to 
            else:
                print(index, "X")
print(found_letters)