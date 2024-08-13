import random

number = random.randint(1,10)
isGuessRight = False

# Exercise 1: Working with a while loop
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# while isGuessRight != True:
#     guess = input("Guess a number between 1 and 10: ")
#     if int(guess) == number:
#         print("You guessed {}. That is correct! You win!".format(guess))
#         isGuessRight = True
#     else:
#         print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))


# Informing the user about the script
print("Count  1 to 10!")

# Writing the for loop
for x in range (1, 11):
    print(f"{x} of 10")