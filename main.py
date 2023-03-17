#import the random library function
import random

# Set the range of numbers
MIN_NUMBER = 1
MAX_NUMBER = 20

# Generates a random number to guess
hidden_number = random.randint(MIN_NUMBER, MAX_NUMBER)

print("Welcome to the number guessing game!")
print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}. Can you guess what it is?")

#The player  is allowed to make up to guesses <= 6
for i in range(1, 7):
    print(f"Guess No {i}: ")
    guess = int(input())

    if guess < hidden_number:
        print("Low!")
    elif guess > hidden_number:
        print("High!")
    else:
        print(f"Congratulations! You guessed the number in {i} guesses!")
        break

# If the player uses all 6 guesses and didn't guess correct number, then it will reveal the hidden number
if guess != hidden_number:
    print(f"Sorry, you ran out of guesses. The secret number was {hidden_number}. Better luck next time!")