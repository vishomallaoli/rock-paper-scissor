import os
import time
import random
from colorama import Fore, init
os.environ['TERM'] = 'xterm'

# Initialize colorama
init(autoreset=True)

# ASCII Art
choices_art = [
    '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''',
    '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''',
    '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
]

choices = ["Rock", "Paper", "Scissors"]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def play_rps(user_choice, scores):
    # Show the user's choice text and art
    print("You chose:")
    print(choices_art[user_choice])
    time.sleep(1)
    clear_screen()

    # Random computer choice
    comp_choice = random.randint(0, 2)

    # Get line-by-line art for both choices
    user_art_lines = choices_art[user_choice].split('\n')
    comp_art_lines = choices_art[comp_choice].split('\n')

    # Show both choices side-by-side
    print("You chose:                           Computer chose:")
    for ua, ca in zip(user_art_lines, comp_art_lines):
        print(f"{ua:35} {ca}")

    # Check result
    if user_choice == comp_choice:
        result = f"{Fore.YELLOW}You've drawn."
    elif (user_choice - comp_choice) % 3 == 1:
        result = f"{Fore.GREEN}You've won!"
        scores['user'] += 1
    else:
        result = f"{Fore.RED}You've lost."
        scores['computer'] += 1

    print(result)
    print(f"\n{Fore.CYAN}Score: You {scores['user']} - {scores['computer']} Computer\n")
    return scores


# Main game logic
scores = {'user': 0, 'computer': 0}

while True:
    print(
        f"{Fore.BLUE}What do you choose? Type {Fore.WHITE}0{Fore.BLUE} for Rock, {Fore.WHITE}1{Fore.BLUE} for Paper, {Fore.WHITE}2{Fore.BLUE} for Scissors, or {Fore.WHITE}'q'{Fore.BLUE} to quit")
    try:
        user_choice = input()

        if user_choice == 'q':
            print(
                f"{Fore.MAGENTA}Thanks for playing! Final Score: You - {scores['user']}, Computer - {scores['computer']}")
            break

        user_choice = int(user_choice)
        if user_choice not in [0, 1, 2]:
            raise ValueError

        scores = play_rps(user_choice, scores)
        input("Press Enter to continue...")  # Pause before clearing screen for next round
        clear_screen()
    except ValueError:
        print(f"{Fore.RED}Invalid input! Please enter a valid number (0, 1, or 2) or 'q' to quit.")
