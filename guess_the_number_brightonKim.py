# Importing randomness in order to create a number
import random

# Guesses start from 0
guesses = 0

# Gives a number between 1 and 500
number = random.randint (1,500)

# Prints the description of the game
print """Welcome to 'Guess the Number Game'!
Now you are going to guess the number between 1 and 500!
What is your guess?"""

# While loop that lasts until 30 chances
while guesses < 30:

    # Makes the player input the number
    guess = int(raw_input("> "))

    # Number of guesses increases one by one as they guess
    guesses += 1

    # Tells the player that the guessed number is smaller than the number given
    if guess < number:
        print "Your guess is too low."

    # Tells the player that the guessed number is higher than the number given
    elif guess > number:
        print "Your guess is too high."

    # If they guess the number, exits from the while loop
    elif guess == number:
        break

# Above guess == number statement just went out of the while loop, but this one prints out that the player had guessed the right number
if guess == number:
    guesses = str(guesses)
    print "You are correct! \nYou guessed my number in " + guesses + " guesses."

# If 30 chances are over and the player still could not get the number, this text will appear.
elif guess != number:
    print "The chances are over! Try next time."
