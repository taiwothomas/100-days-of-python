from replit import clear
#HINT: You can call clear() to clear the output in the console.
from BlindAuctionart import logo
print(logo)

print("Welcome to the secret auction.")

other  = 'yes'
auction = []
while other == 'yes':
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  new_bid = {}
  new_bid["name"] = name
  new_bid["bid"] = bid
  auction.append(new_bid)
  other = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if other == 'yes':
    clear()
  elif other == 'no':
    n = 0
    winner = auction[1]
    for thing in auction:
      if winner["bid"] < auction[n]["bid"]:
        winner = auction[n]
      n += 1
    print(f"The winner of the auction is {winner['name']} with bid ${winner['bid']}.")