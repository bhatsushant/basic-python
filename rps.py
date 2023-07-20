import random
import sys
from enum import Enum


def rps():
    player_choice = int(
        input('Please enter your input\n1 for Rock\n2 for Paper\n3 for Scissor\n\n'))

    if player_choice not in [1, 2, 3]:
        print('You can only enter the numbers 1, 2 or 3')
        rps()

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3

    computer_choice = int(random.choice('123'))

    print(f'You chose {(RPS(player_choice))} and computer chose {RPS(computer_choice)}'.replace(
        'RPS.', ''))

    if computer_choice == 1 and player_choice == 2:
        print('🎉 You win!')
    elif computer_choice == 2 and player_choice == 3:
        print('🎉 You win!')
    elif computer_choice == 3 and player_choice == 1:
        print('🎉 You win!')
    elif computer_choice == player_choice:
        print('😲 It\'s a tie!')
    else:
        print('🐍 Python wins!')

    print("\nPlay again?")
    while True:
        play = input("\nPress Y to play again or any other key to exit.\n")
        if play.lower() == "y":
            rps()
        else:
            print("\n🎉🎉🎉\nThank you for playing!\n")
            sys.exit("\nBye!👋")


rps()
