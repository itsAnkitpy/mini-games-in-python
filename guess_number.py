import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    level = input('Please select the difficulty level - Type easy or hard - ')
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_answer(guess,random_number,turns):
    if guess > random_number:
        print("Too High!!")
        return turns - 1
    elif guess <  random_number:
        print("Too Low!!")
        return turns - 1
    else:
        print(f'You guessed correctly. The selected number was {random_number}')
        print('Thank you for playing.You can try some other games here as well')
        print('\n')


def guess_the_number(x):
    print("Let's play Guess the Number")

    random_number = random.randint(0,x)

    print('\n')


    # For setting up the difficulty level for this game
    turns = set_difficulty()
    print(f'You have {turns} attempts to guess the number.')
    print('\n')

    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 0 and {x}:  "))
        
        # Verifying if the guess is correct
        turns = check_answer(guess,random_number,turns)
        


        if turns == 0:
            print('You have ran out of attempts. YOU LOSE')
            break

        elif guess != random_number:
            print(f'You have {turns} attempts to guess the number.')
            print("Guess again")
            print('\n')


    