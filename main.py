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


# Declatre a function deal() that computer deal a card to player or computer.
def deal():
  """Deal a random card from the deck."""
  card = random.choice(deck_list)
  return card

# Declare a function to get the initial score_list of the cards.
def score(card_list):
  """This funciton takes an input parameter "cards_list", which could be assigned in player_cards or dealer_cards. The return value is called 'score_list', which could be stored in player_score list or dealer_score list."""
  score_list = []
  for i in range(len(card_list)):
    # Notice: deck_score is a dictionary, we get the card scores in the deck using the card string as the key.
    score = deck_score[card_list[i]]
    score_list.append(score)
  return score_list

# Declare another function to sum up a score_list's score
def total_score(score_list):
  """Use this function to sum up the scores."""
  return sum(score_list)

# Declare a function to let user decide whether to add a card or not. 
def Hit_or_Stand():
  player_choice = input("Enter 'H' to hit a card, or type 'S' to stand: ").lower()
  if player_choice == 'h':
    return True
  elif player_choice == 's':
    return False
  else:
    print("Invalid input, please enter your choice again. :)")
    return Hit_or_Stand()
  
# Declare a funtion which could change the score of Ace when bust. ####TODO
def swap_Ace_score():
  return 

def play():
  """Ask user play or not, or if play again."""
  play_game = input("Do you want to play Blckjack? Type 'Y' or 'N': ").lower()
  if play_game == 'y':
    return True
  elif play_game == 'n':
    return False
  else:
    return play()

####Code of Game display starts here!!!####    
print(art.logo)
#Do you want to play Blackjack?
play_blackjack = play()
while play_blackjack:
  # Game start:
  # Create two lists to store the user and dealer's hands.
  player_cards = []
  player_score_list = []
  dealer_cards = []
  dealer_score_list = []

  # Deal 2 cards to the user.
  for _ in range(2):
    new_card = deal()
    player_cards.append(new_card)

  # Deal 2 cards to the dealer, show one and hide one card.
  for _ in range(2):
    new_card = deal()
    dealer_cards.append(new_card)

  player_score_list = score(player_cards)
  player_score = total_score(player_score_list)
  #  Show player's hand info:
  #Check if player got Blackjack or 2 Aces?
  if player_score == 22:
    player_score_list.remove(11).append(1)
  print(f"Your cards: {player_cards}, current score: {player_score}")
  if player_score == 21:
    print("Blackjack! You Win!  🎉 🏆 😄\n")
    ### TODO: Bypass the rest of codes and restart###
  else:
    print(f"Dealer's cards: [{dealer_cards[0]}, ***]")

  # Player make choice, deal cards, and calculate the scores:
  Hit = Hit_or_Stand()
  while Hit:
    new_card = deal()
    player_cards.append(new_card)
    player_score_list = score(player_cards)
    player_score = total_score(player_score_list)
    ##TODO: Ace condition
    if player_score > 21:
      if 11 in player_score_list:
        player_score_list.remove(11)
        player_score_list.append(1)
        player_score = total_score(player_score_list)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        Hit = Hit_or_Stand()
      else:
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print("BUST")
        Hit = False
    elif player_score == 21:
      print(f"Your cards: {player_cards}, current score: {player_score}")
      print("You Got 21")
      Hit = False
    else:
      print(f"Your cards: {player_cards}, current score: {player_score}")
      Hit = Hit_or_Stand()

  print("It's Dealer's turn...")
  ## Dealer's hand auto deal:
  dealer_score_list = score(dealer_cards)
  dealer_score = total_score(dealer_score_list)
  ####Run Debug code:###
  # print(f"(Debug) Dealer's cards: {dealer_cards}")
  if player_score == 21:
    #Show both cards & score, then declare player wins!
    print(f"Dealer's cards: {dealer_cards}, dealer's score: {dealer_score}")
    if dealer_score == 21:
      print("Dealer got Blackjack! You Lose...😢\n")
    else:
      print("You Win! 🎉 🏆 😄\n")
  elif player_score >21:
    print(f"Dealer's cards: {dealer_cards}, dealer's score: {dealer_score}\nYou Lose...😢\n")
  else:
    ## Compare and show results
    if dealer_score == 21:
      print(f"Dealer's cards: {dealer_cards}, dealer's score: {dealer_score}\nDealer got Blackjack! You Lose...😢\n")
    else:
      while dealer_score < player_score:
        new_card = deal()
        dealer_cards.append(new_card)
        dealer_score_list = score(dealer_cards)
        dealer_score = total_score(dealer_score_list)
        #Check if there's Ace?
        if dealer_score > 21 and 11 in dealer_score_list:
          dealer_score_list.remove(11)
          dealer_score_list.append(1)
          dealer_score = total_score(dealer_score_list)
          ####TODO: Bug's here!!!####
          print(f"(Ace)Dealer's cards: {dealer_cards}")
        elif dealer_score > 21:
          print(f"Dealer's cards: {dealer_cards}, dealer's score: {dealer_score}\nDealer BUST! You Win! 🎉 🏆 😄\n")
            ##Jump out to the end
      if dealer_score == player_score:
        print(f"Dealer's cards: {dealer_cards}, dealer's score: {dealer_score}\nIt's a tie. 🤣\n")
      elif dealer_score < 21:
        print(f"Dealer's cards: {dealer_cards}, dealer's score: {dealer_score}\nDealer got higher score. You Lose...😢\n")

  play_blackjack = play()
  clear()
  print(art.logo)

clear()
print("Goodbye~")
