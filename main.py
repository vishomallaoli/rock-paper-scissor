import random
import time

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


def play_rps(user_choice):
    print(f"You chose:\n{choices_art[user_choice]}")

    comp_choice = random.randint(0, 2)
    time.sleep(1)  # Pause for a moment before revealing computer's choice
    print(f"Computer chose:\n{choices_art[comp_choice]}")

    if user_choice == comp_choice:
        return "You've drawn."
    elif (user_choice - comp_choice) % 3 == 1:
        return "You've won."
    else:
        return "You've lost."


# Main game logic
while True:
    try:
        user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, or 'q' to quit\n")

        if user_choice == 'q':
            print("Thanks for playing! Goodbye.")
            break

        user_choice = int(user_choice)
        if user_choice not in [0, 1, 2]:
            raise ValueError

        print(play_rps(user_choice))
        time.sleep(1)  # A small pause to let user read the result
    except ValueError:
        print("Invalid input! Please enter a valid number (0, 1, or 2) or 'q' to quit.")
