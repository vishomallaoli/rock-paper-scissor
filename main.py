rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
x = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
# x represents human choice.
print("You chose:")

# I want to map the ASCII art with the 0, 1, or 2 that the user prints.
if x == 0:
  print(rock)
elif x == 1:
  print(paper)
elif x == 2:
  print(scissors)

# y represents computer choice.
y = random.randint(0 , 2)
print("Computer Chose:")

# I want to may the ASCII art with the 0, 1, or 2 that the computer chooses randomly.
if y == 0:
  print(rock)
elif y == 1:
  print(paper)
elif y == 2:
  print(scissors)



# there are only 3 combinations as (0, 1), (1, 2), and (2, 0) for you to win and same three combination for you to lose and same 3 combination for you to draw.
# if (x, y) represents the set of winning, then (y, x) represents the set of losing. (x, x) is the set of draw.

if x < 0 or x > 2:
  print("You've typed an invalid number.")
elif x == 0 and y == 2 or x == 2 and y == 1 or x == 1 and y == 0:
  print("You've won.")
elif x == y:
  print("You've drawn.")
else:
  print("You've lost.")

