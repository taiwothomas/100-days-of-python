import random
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

player_cards = [draw(), draw()]
dealer_cards = [draw(), draw()]
print(f"You drew {player_cards}.")
print(f"Dealer drew [{dealer_cards[1]}] +1.")
player_total = card_sum(player_cards)
if player_total < 21:
  deal = input("Do you want to draw another card? 'yes' or 'no'? ")

while deal == 'yes' and player_total < 21:
  player_cards.append(draw())
  print(player_cards)
  deal = input("Do you want to draw another card? 'yes' or 'no'? ")
  player_total = card_sum(player_cards)

dealer_total = card_sum(dealer_cards)
player_hand = f"You have {player_total}: {player_cards}"
dealer_hand = f"Dealer has {dealer_total}"

if dealer_total <= 17 and dealer_total < player_total:
  dealer_cards.append(draw())
elif dealer_total > 17 and dealer_total < player_total and player_total < 21:
  dealer_cards.append(draw())

dealer_total = card_sum(dealer_cards)
dealer_hand = f"Dealer has {dealer_total}: {dealer_cards}"

if player_total == 21 and dealer_total != 21:
  print("21! You win!")
elif player_total < 21 and (player_total > dealer_total or dealer_total > 21):
  print(f"{player_hand}. {dealer_hand}. You win!")
elif dealer_total <= 21 and (dealer_total > player_total or player_total > 21):
  print(f"{player_hand}. {dealer_hand}. You lose.")
else:
  print(f"{player_hand}. {dealer_hand}. It's a draw.")

#you have 21
#you have more than dealer below 21
#dealer is above 21