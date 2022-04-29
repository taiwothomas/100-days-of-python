import random
from replit import clear
from HigherLower_data import *

guess = True
score = 0
choice = ''

def options(list):
  """Picks a random option from a list."""
  unique = list[random.randint(0,len(list)-1)]
  return unique

A = options(data)
B = options(data)

while guess:
  print(logo)
  if choice != '':
    print(f"You're right! Your score is {score}")
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
  print(vs)
  print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
  
  choice = ''
  while choice != 'A' and choice != 'B':
    choice = input("Who has more followers? Type 'A' or 'B'. ")
  answer = A['follower_count'] > B['follower_count']
  
  if (answer and choice == 'A') or (not answer and choice == 'B'):
    score += 1
    A = B
    B = options(data)
    clear()
  else:
    clear()
    print(logo)
    guess = 0
    print(f"You're wrong! Your final score is {score}.")