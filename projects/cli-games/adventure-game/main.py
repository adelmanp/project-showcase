#!/usr/bin/env python3

import time
import random


def print_sleep(message):
    print(message)
    time.sleep(1)


def intro(monster, weapon):
    print_sleep("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_sleep("Rumor has it that a " + monster +
                " is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_sleep("In front of you is a house.")
    print_sleep("To your right is a dark cave.")
    print_sleep("In your hand you hold your trusty "
                "(but not very effective) " + weapon + "\n")


def field(monster, weapon):
    print_sleep("Enter 1 to knock on the door of the house. ")
    print_sleep("Enter 2 to peer into the cave. ")
    path = input("What would you like to do? \n"
                 "(Please enter 1 or 2). \n")
    if "1" in path:
        house(monster, weapon)
    elif "2" in path:
        cave(monster, weapon)
    else:
        print_sleep("Unfortantley we don't have time for a side quest, "
                    "which path do you want to go on?")
        field(monster, weapon)


def house(monster, weapon):
    print_sleep("You approach the door of the house.")
    print_sleep("You are about to knock when the door opens "
                "and out steps a " + monster + ".")
    print_sleep("Eep! This is the " + monster + "'s house!")
    print_sleep("The " + monster + " attacks you!")
    if weapon == "sword":
        battle(monster, weapon)
    else:
        print_sleep("You feel a bit un-prepard for this, what with "
                    "only having a tiny " + weapon + ".")
        battle(monster, weapon)


def battle(monster, weapon):
    fight_or_flight = input("Would you like to (1) fight or (2) run away? \n")
    if "1" == fight_or_flight:
        games_end(monster, weapon)
    elif "2" == fight_or_flight:
        print_sleep("You run back out to the field")
        field(monster, weapon)
    else:
        print("This is not a time for games, "
              "quickly you must make a decision?")
        battle(monster, weapon)
    return fight_or_flight


def games_end(monster, weapon):
    if "sword" == weapon:
        print_sleep("As the " + monster + " moves to attack, "
                    "you unsheath your new sword.")
        print_sleep("The Sword of Ogoroth shines brightly in your hands "
                    "as you brace yourself for the attack.")
        print_sleep("But the " + monster + " takes one look at your "
                    "shiny new toy and runs away!")
        print_sleep("You have rid the town of the " + monster +
                    ". you are victorious!")
        play_again()
    else:
        print_sleep("You do your best...")
        print_sleep("but your " + weapon +
                    " is no match for the " + monster)
        print_sleep("You have been defeated!")
        play_again()


def cave(monster, weapon):
    if weapon == "sword":
        print_sleep("You peer cautiously into the cave.")
        print_sleep("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
        print_sleep("You walk back out to the field")
        field(monster, weapon)
    else:
        print_sleep("You peer cautiously into the cave.")
        print_sleep("It turns out to be only a very small cave.")
        print_sleep("Your eye catches a glint of metal behind a rock")
        print_sleep("You have found the magical Sword of Ogoroth!")
        print_sleep("You discard your silly old " + weapon +
                    " and take the sword with you.")
        print_sleep("You walk back out to the field")
        weapon = "sword"
        field(monster, weapon)


def play_again():
    again = input("Would you like to play again? (y/n) \n").lower()
    if again == "y":
        start_game()
    elif again == "n":
        print_sleep("Thanks for playing! See you next time.")
    else:
        print_sleep("invalid selection, please pick again")
        play_again()


def start_game():
    monster_options = ["dark elf", "dragon", "gorgon",
                       "troll", "goblin", "orc"]
    monster = random.choice(monster_options)
    weapon_options = ["dagger", "stick", "torch", "rock"]
    weapon = random.choice(weapon_options)
    intro(monster, weapon)
    field(monster, weapon)


start_game()
