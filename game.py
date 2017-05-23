"""A number-guessing game."""

# greet player
# get player name
# choose random number between 1 and 100
# repeat forever:
#     get guess
#     if guess is incorrect:
#         give hint
#         increase number of guesses
#     else:
#         congratulate player

import random

name = raw_input("Welcome, what is your name? ")
print "Hello, %s, do you want to play a guessing game? " %(name)

random_number = random.randint(1,101)
user_guess = 0
count = 0
while user_guess != random_number:
    user_guess = int(raw_input("Guess a number from 1 to 100: "))
    if user_guess > random_number:
        print "Your guess is too high!"
        count += 1
    elif user_guess < random_number:
        print "Your guess is too low!"
        count += 1
    else:
        print "Well done, %s, You found the number in %s trials!" %(name,count)