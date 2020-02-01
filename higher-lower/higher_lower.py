# This is a comment
# Imported libraries go here
import random
# Global variables go here
game_on = None
guess = None

secret = None
# Function for easy version
def difficulty_level_easy():
    global secret
    secret = int(random.randrange(0, 100))
    while game_on:
        guess = int(input('Guess a number. '))
        if guess > secret:
            print('Your guess is too high. Try again.')
        elif guess < secret:
            print('Your guess is too low. Try again.')
        elif guess == secret:
            print('You win!')
            play_again()

# Function for hard version
def difficulty_level_hard():
    global secret
    secret = int(random.randrange(0, 100))
    global guess
    guess = 3
    for i in range(guess):
        guess = int(input('Guess a number. '))
        if i == 2:
            print('Game over. Too many guesses.')
            play_again()
        elif guess > secret:
            print('your guess is too high. Try again.')
        elif guess < secret:
            print('your guess is too low. Try again.')
        elif guess  == secret:
            print('You win!')
            play_again()

# Function to start game
def start_game():
    global game_on
    game_on = True  
    level = input('Welcome. Type easy, hard, or quit. ')
    if level == 'easy':
        difficulty_level_easy()
    elif level == 'hard':
        difficulty_level_hard()
    elif level == 'quit':
        game_on = False
        print('Thanks for playing.')

# Function to stop game
def play_again():
    global game_on
    game_on = True
    play = input('Play again? Yes or No. ')
    if play == 'Yes':
        start_game()
    else:
        game_on = False
        print('Thanks for playing.')

start_game()
# Function calls go here