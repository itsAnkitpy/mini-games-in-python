import random
from hangman_art import logo,stages
from hangman_words import word_list



def hangman_game():

    print(logo)
    end_of_game = False
    lives = len(stages) - 1

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    # Just to cross check our working of code
    # print(f"The selected word is {chosen_word}")

    display = []
    for i in range(word_length):
        display += "_"
    print(display)    

    # The main program begins from here
    while not end_of_game:

        guess = input("Please guess a letter - ")
        if guess in display:
            print(f"You have already guessed this letter {guess}")

        for position in range(word_length):
            letter = chosen_word[position]    
            if letter == guess:
                display[position] = letter
        print(display)     
        print('\n')   

        if guess not in chosen_word:
            print(f"You guessed the letter {guess} which is not in the word. You lose a life")
            lives -= 1
            print(f'You have {lives} attempts left.')
            if lives == 0:
                end_of_game = True
                print("You lose")

            print(stages[lives])

        if "_" not in display:
            end_of_game = True
            print("You win.You guessed the word correctly")   
            print("Thanks for playing \n")     

        