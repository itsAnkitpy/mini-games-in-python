import os
os.system('cls')

from guess_number import guess_the_number
from rps import rock_paper_scissors


# More Games to be added
while True:
    txt = """Welcome to Mini Games!!!
    - Guess The Number (1)
    - Rock, Paper, Scissors (2)
    - Wordle (3)
    - ConnectFour (4)
    - Tic Tac Toe (5)
Select a game (press a number or 'q' to quit): """
                           
    value = input(txt)

    if value == "1": 
        upper_range = int(input("Please select the upper value range for this game - "))
        print('\n')
        guess_the_number(upper_range)

    elif value == "2":
        rock_paper_scissors()

    elif value == "q":
        print('Thanks for playing Mini Games')
        break
        