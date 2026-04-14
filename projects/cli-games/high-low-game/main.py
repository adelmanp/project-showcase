#!/usr/bin/python3

import random
import game_data
import art
from os import system

keep_playing = True
score = 0

def choose_a():
  return random.choice(game_data.data)

def choose_b(option_a):
  option_b = random.choice(game_data.data)
  while option_a == option_b:
    option_b = random.choice(game_data.data)
  return option_b

def check_followers(option_a, option_b, play_choice):
  a_follers = option_a['follower_count']
  b_follers = option_b['follower_count']
  # print(f"[DEBUG] total followers a_follers: {a_follers} b_follers {b_follers}")
  if a_follers > b_follers and play_choice == 'a':
    # print(f"[DEBUG] A wins, a_follers: {a_follers}, play_choice: {play_choice}, score: {score}")
    return option_a
  elif b_follers > a_follers and play_choice == 'b':
    # print(f"[DEBUG] B wins, b_follers: {b_follers}, play_choice: {play_choice}, score: {score}")
    return option_b
  else:
    return "game_over"

def display_score(score):
  if keep_playing:
    system('clear')
    print(art.logo)
    print(f"Your right! Current score: {score}")
  else:
    system('clear')
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")

def dispaly_compariosn(option_a, option_b):
  # print(f"[DEBUG] option_a = {option_a}") 
  # print(f"[DEBUG] option_b = {option_b} \n")
  print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']} ")
  print(art.vs)
  print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']} ")
  
print(art.logo)

a = choose_a()
b = choose_b(a)
# print(f"[DEBUG] option_a: {a} \n")
# print(f"[DEBUG] option_b: {b}")
while keep_playing:
  dispaly_compariosn(a, b)
  play_choice = input("Who has more followers? Type 'A' or 'B'").lower()
  answer = check_followers(a, b, play_choice)
  if answer == a:
    score += 1
    b = choose_b(a)
    display_score(score)
  elif answer == b:
    score += 1
    a = b
    b = choose_b(a)
    display_score(score)
  elif answer == "game_over":
    keep_playing = False
    display_score(score)
  
  