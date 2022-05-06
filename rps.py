import random

def rock_paper_scissors():

    game_tools = ['Rock','Paper','Scissors']

    # User Choice
    user_choice = int(input('Type 0 to select Rock, 1 for Paper and 2 for selecting scissors - '))

    print(f"User choice: {game_tools[user_choice]}")


    # Computer Choice
    computer_choice = random.randint(0,2)

    print(f"Computer choice: {game_tools[computer_choice]}")

    # Final winner
    if user_choice >= 3 or user_choice < 0:
        print("Invalid choice")
        print('\n')
    elif user_choice == 0 and computer_choice == 2:
        print("You Win")
        print('\n')
    elif computer_choice == 0 and user_choice == 2:
        print("Computer Wins")
        print('\n')
    elif user_choice > computer_choice:
        print("You Win")
        print('\n')
    elif computer_choice > user_choice:
        print("Computer Wins")
        print('\n')
    else:
        print("It's a DRAW.")
        print('\n')


