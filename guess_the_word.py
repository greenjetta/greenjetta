import random

def guess(x):
    random_number = random.randint(50, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 50 and {x}: '))
        if guess < random_number:
            print('no too low')
        elif guess > random_number:
            print('no too high')

    print('yay u got it')

guess(100)












