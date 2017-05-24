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
greeting = "Hello, %s, do you want to play a guessing game? " %(name)
print greeting
best_score = ""

def number_game():
    random_number = random.randint(1,100)
    user_guess = 0
    count = 0
    while user_guess != random_number:
        user_guess = raw_input("Guess a number from 1 to 100: ")
        try:
            user_guess = int(user_guess)
            #break
        except ValueError:
            print("Oops! That was an invalid number. Rounding number.")
            user_guess = int(float(user_guess))
            print user_guess

        if user_guess > random_number:
            print "Your guess is too high!"
            count += 1
        elif user_guess < random_number:
            print "Your guess is too low!"
            count += 1
        elif user_guess < 1 or user_guess > 100:
            print "Please enter a number between 1 and 100."
            count += 1
        else:
            print "Well done, %s, You found the number in %s trials!" %(name,count)
    return count

number_game()

    # keep track of best score
greeting = raw_input("Would you like to play another round: ")
if  greeting == 'yes':
    number_game()
    #     if count < best_score:

else:
    print "goodbye"
