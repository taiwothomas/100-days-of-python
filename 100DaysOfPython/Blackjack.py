import random
from Blackjack_art import logo
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw():
  return deck[random.randint(0,12)]

def card_sum(cards):
  total = 0
  for card in cards:
    total += card
  if 11 in cards and total > 21:
    cards[cards.index(11)] = 1
    total = 0
    for card in cards:
      total += card
  return total
game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'. ")

while game == 'y':
  print(logo)
  player_cards = [draw(), draw()]
  dealer_cards = [draw(), draw()]
  player_total = card_sum(player_cards)
  dealer_total = card_sum(dealer_cards)
  print(f"You drew {player_cards}.Your total is {player_total}")
  print(f"Dealer first card is [{dealer_cards[0]}].")
  
  if player_total < 21:
    deal = input("Do you want to draw another card? 'yes' or 'no'? ")
  while deal == 'yes' and player_total < 21:
    player_cards.append(draw())
    player_total = card_sum(player_cards)
    print(f"You have {player_total}: {player_cards}\nDealer's first card is [{dealer_cards[0]}]")
    if player_total < 21:
      deal = input("Do you want to draw another card? 'yes' or 'no'? ")
  
  dealer_total = card_sum(dealer_cards)
  player_hand = f"Your final hand is {player_cards}, with score {player_total}."
  dealer_hand = f"Dealer's final hand is {dealer_cards}, with score {dealer_total}."
  
  if dealer_total <= 17 and dealer_total < player_total:
    dealer_cards.append(draw())
  elif dealer_total > 17 and dealer_total < player_total and player_total < 21:
    dealer_cards.append(draw())
  
  dealer_total = card_sum(dealer_cards)
  dealer_hand = f"Dealer has {dealer_total}: {dealer_cards}"
  
  if player_total == 21 and dealer_total != 21:
    print(f"You have 21! {dealer_hand} You win!")
  elif player_total < 21 and (player_total > dealer_total or dealer_total > 21):
    print(f"{player_hand}. {dealer_hand}. You win!")
  elif dealer_total <= 21 and (dealer_total > player_total or player_total > 21):
    print(f"{player_hand}. {dealer_hand}. You lose.")
  else:
    print(f"{player_hand}. {dealer_hand}. It's a draw.")
  game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'. ")
