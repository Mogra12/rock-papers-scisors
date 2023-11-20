import random
from time import sleep


rps = ['rock', 'papers', 'scisors']

interface = """
Rock
Papers
Scissors
"""


def rps_game():
    print(interface)
    user_choice = input("Enter your choice: ").lower()
    computer_choice = random.choice(rps)
    print(f"Computer choice: {computer_choice}")
    sleep(1)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock' and computer_choice == 'scisors':
        print("You won!")
    elif user_choice == 'rock' and computer_choice == 'papers':
        print("You lost!")
    elif user_choice == 'papers' and computer_choice == 'rock':
        print("You won!")
    elif user_choice == 'papers' and computer_choice =='scisors':
        print("You lost!")
    elif user_choice =='scisors' and computer_choice == 'rock':
        print("You lost!")
    elif user_choice =='scisors' and computer_choice == 'papers':
        print("You won!")


rps_game()