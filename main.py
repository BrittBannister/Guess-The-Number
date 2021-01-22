import random


def guess(x):
    '''Computer generates a secret number for user to guess'''
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high')

    print(f'YAY! Congrats. You guessed the correct number of {random_number}. You win!')


def computer_guess(x):
    '''User has a secret number and computer guesses'''
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'YAY! The computer guessed your number, {guess} correctly!')


computer_guess(10)
# guess(10)
