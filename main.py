import random
import time
from colorama import Fore, Style, init

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


def play_rps(user_choice, scores):
    print(f"You chose:\n{choices_art[user_choice]}")

    comp_choice = random.randint(0, 2)
    time.sleep(1)
    print(f"Computer chose:\n{choices_art[comp_choice]}")

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
        time.sleep(1)
    except ValueError:
        print(f"{Fore.RED}Invalid input! Please enter a valid number (0, 1, or 2) or 'q' to quit.")
