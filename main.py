from colorama import Fore, init
from visuals import display_choice_query, display_goodbye_message, display_invalid_input_message
from game_logic import play_rps
from utility import clear_screen


init(autoreset=True)
scores = {'user': 0, 'computer': 0}

while True:
    display_choice_query(scores)
    try:
        user_choice = input()
        if user_choice == 'q':
            display_goodbye_message(scores)
            break

        user_choice = int(user_choice)
        if user_choice not in [0, 1, 2]:
            raise ValueError

        scores = play_rps(user_choice, scores)
        input("Press Enter to continue...")
        clear_screen()
    except ValueError:
        display_invalid_input_message()
