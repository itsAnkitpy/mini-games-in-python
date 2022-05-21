import random
from rich import print

words = (
    "awake",
    "blush",
    "focal",
    "evade",
    "serve",
    "model",
    "karma",
    "grade",
    "quiet",
)

class Wordle:
    def __init__(self):
        # To generate random word from words above
        self.word = random.choice(words)
        self.num_guesses = 0
        # User will get 6 guesses
        self.guess_dict = {
            0: [" "]*5,
            1: [" "]*5,
            2: [" "]*5,
            3: [" "]*5,
            4: [" "]*5,
            5: [" "]*5,
        }

    def draw_board(self):
        # We just want to print values in the above dictionary
        for guess in self.guess_dict.values():
            print(" | ".join(guess))
            # To clean and separate our each line, acts as a separator 
            print("================")

    def get_user_input(self):

        user_guess = input("Enter a 5 letter word: ").lower()

        # We are strictly asking for 5 letter word as the length of each word above in dict is 5
        while len(user_guess) != 5:
            user_guess = input("Not valid. Please enter a 5 letter word: ")

        for idx, char in enumerate(user_guess):

            if char in self.word:
                # If character at same index value in self.word print in green
                if char == self.word[idx]:
                    # Here we use the rich module to print our output in different colors

                    # If the alphabet is present in the self.word and user guess at same index, we show green
                    char = f"[green]{char}[/]"
                else:
                    # Here we use the rich module to print our output in different colors

                    # If the alphabet is present in the self.word but present in user guess at wrong index, we show yellow
                    char = f"[yellow]{char}[/]"

            self.guess_dict[self.num_guesses][idx] = char

        self.num_guesses += 1
        return user_guess


    def play(self):
        while True:
            # Will draw the board first
            self.draw_board()
            # Will get the value of user guess from above function
            user_guess = self.get_user_input()


            # GAME WON
            if user_guess == self.word:
                self.draw_board()
                print(f"You won! The word was {self.word}")
                print("Thanks for playing \n")
                break
            
            # GAME LOST
            if self.num_guesses > 5:
                self.draw_board()
                print(f"You lost! The word was {self.word}")
                print("Thanks for playing \n")
                break