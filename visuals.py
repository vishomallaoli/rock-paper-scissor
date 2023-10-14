from colorama import Fore

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


def display_choice_query(scores):
    print(f"{Fore.BLUE}What do you choose? Type {Fore.WHITE}0{Fore.BLUE} for Rock, {Fore.WHITE}1{Fore.BLUE} for Paper, {Fore.WHITE}2{Fore.BLUE} for Scissors, or {Fore.WHITE}'q'{Fore.BLUE} to quit")

def display_goodbye_message(scores):
    print(f"{Fore.MAGENTA}Thanks for playing! Final Score: You - {scores['user']}, Computer - {scores['computer']}")

def display_invalid_input_message():
    print(f"{Fore.RED}Invalid input! Please enter a valid number (0, 1, or 2) or 'q' to quit.")
