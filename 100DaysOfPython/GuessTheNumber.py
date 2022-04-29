import random
from GuessTheNumber_art import logo
print(logo)
print("Welcome to the number guessing game.")

number = random.randint(1,100)
choice = 0
print(number)
level = input("Choose a difficulty level: 'easy' or 'hard'. ")
if level == 'easy':
  guesses = 10
elif level == 'hard':
  guesses = 5

while guesses > 0 and choice != number:
  print(f"You have {guesses} attempts remaining to guess the number.")
  choice = int(input("Make a guess: "))
  if choice > number:
    print("Too high!")
  elif choice < number:
    print("Too low!")
  else:
    print("That's correct! You win!")
  guesses -= 1

if guesses == 0:
  print("You've run out of guesses. You lose.")