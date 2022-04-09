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

#Write your code below this line 👇
import random
print("This is a game of Rock, Paper Scissors.")
Human = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors. "))
Human = Human - 1
choice = [rock, paper, scissors]
print("You chose:\n",choice[Human])
Computer = random.randint(0,2)
print("Computer chose:\n",choice[Computer])
Result = Human - Computer
if Result == 0:
  print("It's a draw.")
elif Result > 0 or Result == -2:
  print("Congratulations. You win!")
elif Result < 0 or Result == 2:
  print("Sorry. Computer wins.")