import random
import sys
from enum import Enum

playagain = True
while playagain:
    player_choice = int(
        input('Please enter your input\n1 for Rock\n2 for Paper\n3 for Scissor\n\n'))

    if player_choice < 1 or player_choice > 3:
        print('You can only enter the numbers 1, 2 or 3')
        continue

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

    play = input(
        "\nPlay again?\nPress Y to play again or any other key to exit.\n")
    if play.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉\nThank you for playing!\n")
        playagain = False
sys.exit("\nBye!👋")
