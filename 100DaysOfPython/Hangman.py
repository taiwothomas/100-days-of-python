import random
from hangman_words import *
from hangman_art import *


chosen_word = random.choice(word_list)
result = ""
display = ["_"]*len(chosen_word)
used_letters = []
print(logo)
while result != chosen_word and stages != []:
  guess = input("Guess a letter: ").lower()
  sn = 0
  for i in range(len(chosen_word)):
    if guess in chosen_word[sn]:
      display[sn] = guess
    sn += 1 
  result = ''.join(display)
  if guess in result:
    print("Correct guess!")
  elif guess in used_letters:
    print(f"You have already guessed letter: '{guess}'. You wrong guesses are: {','.join(used_letters)}. Guess again.")
  else: 
    print(f"Wrong guess! '{guess}' is not in this word.")
    print(stages.pop())
    used_letters += guess
  print(result)
  if result == chosen_word:
    print("You win! Game over!")
  elif stages == []:
    print("You lose! Game over!")
    print(f"The correct word is {chosen_word}.")

