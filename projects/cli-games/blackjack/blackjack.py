#!/usr/bin/python3

from os import system
from art import logo
import random

cards = [
  11, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 10, 10, 10,
  11, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 10, 10, 10,
  11, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 10, 10, 10,
  11, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 10, 10, 10
]
player_cards = []
computer_cards = []

def select_player_cards():
  player_cards.append(random.choice(cards))
  player_cards.append(random.choice(cards))
  computer_cards.append(random.choice(cards))
  computer_cards.append(random.choice(cards))

def score_cards(hand_of_cards):
  score = 0 
  for card in hand_of_cards:
    score += card
  if 11 in hand_of_cards and score > 21:
    score -= 10
  return score

def find_winner(user_score, computer_score):
  if computer_score == user_score:
    return "\nDRAW 🙃"
  elif user_score == 21:
    return "\nBlackjack! You win. 😎"
  elif computer_score == 21:
    return "\nYou lose, the dealer has Blackjack 😱"
  elif computer_score > 21:
    return "\nThe dealer has busted, you win! 😃"
  elif user_score > 21:
    return "\nYou Busted! 😭 Game over"
  elif user_score > computer_score:
    return "\nYou Win! 😁"
  else:
    return "\nYou lose 😤"

  
start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n").lower()
system('clear')
print(logo)
# print(f"[DEBUG] player_cards: {player_cards}")
# print(f"[DEBUG] computer_cards: {computer_cards}")
while start == 'y':
  select_player_cards()
  new_cards = "y"
  current_player_score = 0
  while new_cards == "y":
    player_score = score_cards(player_cards)
    if player_score < 22: 
      print(f"  Your cards: {player_cards}, current score: {player_score}")
      print(f"  Computer's first card: {computer_cards[0]}")
      new_cards = input("Type 'y' to get another card, type 'n' to pass: \n")
      system('clear')
      print(logo)
      if new_cards == 'y':
        player_cards.append(random.choice(cards))
      if new_cards == 'n':
        computer_score = score_cards(computer_cards)
        while computer_score < 17:
          computer_cards.append(random.choice(cards))
          computer_score = score_cards(computer_cards)  
        print(f"Your final hand: {player_cards}, final score: {player_score} ")
        print(f"The Computer's final hand: {computer_cards}, final score: {computer_score} ")
        print(find_winner(player_score, computer_score))
    elif player_score > 21: 
      print("You Busted! 😭 Game over")
      print(f"Your cards: {player_cards}, current score: {player_score}")
      new_cards = 'n'

  start = input("\nDo you want to play another game of Blackjack? Type 'y' or 'n': \n").lower()
  if start == 'y':
    player_cards = []
    computer_cards = []
    system('clear')
    print(logo)
  else:
    print("\nThanks for playing Blackjack!")
  