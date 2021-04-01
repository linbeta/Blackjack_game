############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

###############################################################
# I am going challenge the Expert level, and try my best to build a Blackjack game as playing with a real deck of cards.

import art
#Create a dictionary of a poker deck: S for spade, H for heart, D for diamond, and C is for Club.
from poker_deck import deck_list
from poker_deck import deck_score 
import random
from replit import clear

print(art.logo)
def start():
  play_game = input("Do you want to play Blackjack? Type 'Y' or 'N': ").lower()
  if play_game == 'y':
    return True
  elif play_game == 'n':
    return False
  else:
    print("Invalid input, please choose again.")
    start()

in_game = start()

while in_game:
  # Game start, hands delt and show player and computer/dealer's hand.
  pcard1 = random.choice(deck_list)
  pcard2 = random.choice(deck_list)
  phand = [pcard1, pcard2]
  pscore = deck_score[pcard1] + deck_score[pcard2]

  #Make one of the Dealer's card hidden
  dcard_H = random.choice(deck_list)
  dcard1 = random.choice(deck_list)
  dhand = ["*", dcard1]
  dscore = deck_score[dcard_H] + deck_score[dcard1]

  print(f"Your hand: {phand}, current score: {pscore}")
  if pscore == 21 and len(phand) == 2:
    print("Blackjack!")
  elif pscore > 21:
    pscore -= 10
  #Dealer's card  
  print(f"Dealer's hand: {dhand}")

  #Ask player HIT or STAND
  def HorS():
    if pscore == 21:
      return False
    else:
      player_choice = input("Enter 'H' for hit, type 'S' for stand: ").lower()
      if player_choice == 'h':
        return True
      else:
        return False


  # the return value of HorS() will store in variable deal, and that's a key whether the deal module will execute or not.
  deal = HorS()
  # print(deal)

  # Player module
  while deal:
    pcard_new = random.choice(deck_list)
    phand.append(pcard_new)
    pscore += deck_score[pcard_new]
    #Use this line to show player's current hand and acore:
    print(f"Your hand: {phand}, current score: {pscore}")
    if pscore == 21:
      print("Blackjack!")
      deal = False
    elif pscore > 21:
      # Make Ace score count as 11 or 1
      if deck_score[pcard1] == 11 or deck_score[pcard2] == 11:
        pscore -= 10
      elif deck_score[pcard_new] == 11:
        pscore -= 10
      ###TODO: Need to work on another statement if there's an Ace in the phand list.###
      # elif 
      # Otherwise when there's no Aces
      else:
        print("Bust!")
        deal = False
    else:
      deal = HorS()

  # print("Wait for computer and compare.")
  # Computer / Dealer module
  dhand = [dcard_H, dcard1]
  # print(f"Dealer's hand: {dhand}, dealer score: {dscore}")

  # note: when pscore == 21, count as player wins.
  # We'll deal with the score of 21 tie condition.
  if pscore > 21:
    print(f"Dealer's hand: {dhand}, dealer score: {dscore}")
    print(f"Your score is {pscore}, which is BUST, YOU LOSE...\n")
  elif pscore == 21:
    print(f"Dealer's hand: {dhand}, dealer score: {dscore}")
    print("You got Blackjack! YOU WIN!!!")
    #Dealer module
    #Compare module
  else:
    #Dealer module
    while dscore < 17:
      dcard_new = random.choice(deck_list)
      dhand.append(dcard_new)
      dscore += deck_score[dcard_new]
    print(f"Dealer's hand: {dhand}, dealer score: {dscore}")
    #Compare module
    if dscore > 21:
      print("Dealer BUST, You win!\n")
    elif dscore == 21:
      print("Dealer got Blackjack, You LOSE...\n")
    elif dscore <21 and dscore > pscore:
      print(f"Your score is {pscore}, You LOSE...\n")
    elif dscore == pscore:
      print("It's a tie.\n")
    elif dscore < pscore:
      print(f"Your score is {pscore}, YOU WIN!!!!\n")
  
  play_again = input("Play again? Type 'Y' or 'N': ").lower()
  if play_again == 'y':
    in_game = True
    clear()
    print(art.logo)
  elif play_again == 'n':
    in_game = False
  else:
    print("Invalid input.")
    in_game = False

clear()
print("Goodbye~")

# Questions:
# Ace condition debug: How to optimize the usage of Ace?
# eg. Your hand: ['2_D', '5_S', 'Ace_D', '2_C', '9_S'], current score: 29