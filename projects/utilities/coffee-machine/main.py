#!/usr/bin/python3

from common import menu, machine_resources
from sys import exit
from math import ceil
import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


system_power = True
coins = {
    "quarters": 10,
    "dimes": 10,
    "nickles": 10,
    "pennies": 10,
}


def take_order():
    """
    Takes drink order for vending machine
    :return:
    """
    print(f"\nMenu: \nEspresso, cost: ${menu['espresso']['cost']} \nlatte, cost: ${menu['latte']['cost']} \ncappuccino, cost: ${menu['cappuccino']['cost']}")
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return drink


def add_machines_change(quarters, dimes, nickles, pennies):
    """
    sorts the money into the machine by coin
    :param quarters:
    :param dimes:
    :param nickles:
    :param pennies:
    :return:
    """
    add_quarters = coins['quarters'] + quarters
    coins['quarters'] = add_quarters
    add_dime = coins['dimes'] + dimes
    coins['dimes'] = add_dime
    add_nickle = coins['nickles'] + nickles
    coins['nickles'] = add_nickle
    add_pennie = coins['pennies'] + pennies
    coins['pennies'] = add_pennie
    logger.debug(f"Machine's change: {coins}")


def subtract_machines_change(quarters, dimes, nickles, pennies):
    """
    subtracts the conis from the machine to refund customer
    :param quarters:
    :param dimes:
    :param nickles:
    :param pennies:
    :return:
    """
    logger.debug(f"Returning Quarters: {quarters}, Dimes: {dimes}, Nickles: {nickles}, Pennies: {pennies}")
    subtract_quarters = coins['quarters'] - quarters
    coins['quarters'] = subtract_quarters
    subtract_dime = coins['dimes'] - dimes
    coins['dimes'] = subtract_dime
    subtract_nickle = coins['nickles'] - nickles
    coins['nickles'] = subtract_nickle
    subtract_pennie = coins['pennies'] - pennies
    coins['pennies'] = subtract_pennie
    logger.debug(f"Machine's change: {coins}")


def provide_change(owed, paid, quarters_used, dimes_used, nickles_used, pennies_used):
    return_quarters = 0
    return_dimes = 0
    return_nickles = 0
    return_pennies = 0
    if paid > owed:
        logger.debug(f"Owe Change")
        change_owed = round(paid - owed, 2)
        change_owed_rounded = int(change_owed * 100)
        logger.debug(f"Refund Amount: {change_owed_rounded} cents")

        while change_owed_rounded >= 25 and coins['quarters'] > 0:
            change_owed_rounded -= 25
            return_quarters += 1
        logger.debug(f"return_quarters: {return_quarters}")
        logger.debug(f"Amount due after returning quarters: {change_owed_rounded}")

        while change_owed_rounded >= 10 and coins['dimes'] > 0:
            change_owed_rounded -= 10
            return_dimes += 1
        logger.debug(f"return_dimes: {return_dimes}")
        logger.debug(f"Amount due after returning dimes: {change_owed_rounded}")

        while change_owed_rounded >= 5 and coins['nickles'] > 0:
            change_owed_rounded -= 5
            return_nickles += 1
        logger.debug(f"return_nickles: {return_nickles}")
        logger.debug(f"Amount due after returning nickles: {change_owed_rounded}")

        while change_owed_rounded >= 1 and coins['pennies'] > 0:
            change_owed_rounded -= 1
            return_pennies += 1
        logger.debug(f"return_pennies: {return_pennies}")
        logger.debug(f"Amount due after returning pennies: {change_owed_rounded}")

        logger.debug(f"change owned should = 0 Change Owed: {change_owed_rounded}")
        subtract_machines_change(return_quarters, return_dimes, return_nickles, return_pennies)
    elif paid < owed:
        subtract_quarters = coins['quarters'] - quarters_used
        coins['quarters'] = subtract_quarters
        subtract_dime = coins['dimes'] - dimes_used
        coins['dimes'] = subtract_dime
        subtract_nickle = coins['nickles'] - nickles_used
        coins['nickles'] = subtract_nickle
        subtract_pennie = coins['pennies'] - pennies_used
        coins['pennies'] = subtract_pennie
        logger.debug(f"Machine's change: {coins}")


def take_payment(drink):
    """
    Takes payment and check if amount is correct
    :param drink:
    :return:
    """
    amount_due = menu[drink]['cost']
    logger.debug(f"Amount due: {amount_due}")
    print("PLease insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    payment = round((quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01), 2)
    logger.debug(f"Amount paid: {payment}, quarters: {quarters}, dimes: {dimes}, nickles: {nickles}, pennies: {pennies},")
    add_machines_change(quarters, dimes, nickles, pennies)
    if payment == amount_due:
        return True
    if payment > amount_due:
        change = round(payment - amount_due, 2)
        provide_change(amount_due, payment, quarters, dimes, nickles, pennies)
        format_change = "{:.2f}".format(change)
        print(f"\nHere is ${format_change} in change. ")
        return True
    if payment < amount_due:
        provide_change(amount_due, payment, quarters, dimes, nickles, pennies)
        print("Sorry that's not enough money. Money refunded")
        return False


def check_resources(drink):
    required = True
    recipe = menu[drink]['ingredients']
    logger.debug(f"Ingredients needed: {recipe}")
    if machine_resources['water'] >= recipe['water']:
        machine_resources['water'] -= recipe['water']
        logger.debug(
            f"Removing {recipe['water']}ml of water. Machine has {machine_resources['water']}ml of water remaining"
        )
    else:
        print(f"Sorry there is not enough water")
        required = False
    if machine_resources['milk'] >= recipe['milk']:
        machine_resources['milk'] -= recipe['milk']
        logger.debug(
            f"Removing {recipe['milk']}ml of water. Machine has {machine_resources['milk']}ml of water remaining"
        )
    else:
        print(f"Sorry there is not enough milk")
        required = False
    if machine_resources['coffee'] >= recipe['coffee']:
        machine_resources['coffee'] -= recipe['coffee']
        logger.debug(
            f"Removing {recipe['coffee']}ml of water. Machine has {machine_resources['coffee']}ml of water remaining"
        )
    else:
        print(f"Sorry there is not enough coffee")
        required = False
    return required


def make_order(drink):
    print(f"\nHere is your {drink}. Enjoy!")


while system_power:
    order = take_order()
    if order == "off":
        system_power = False
        # exit(0)
    elif order == "report":
        print(f"\nSystem Report")
        print(f"Water: {machine_resources['water']}")
        print(f"Milk: {machine_resources['milk']}")
        print(f"Coffee: {machine_resources['coffee']}")
        machine_money = (coins['quarters'] * .25) + (coins['dimes'] * .1) + (coins['nickles'] * .05) + (coins['pennies'] * .01)
        format_money = "{:.2f}".format(machine_money)
        print(f"Money: ${format_money}")
        print(f"Coins in the machine:")
        print(f"Quarters: {coins['quarters']} Dimes: {coins['dimes']} Nickles: {coins['nickles']} Pennies {coins['pennies']}")
    else:
        paid = take_payment(order)
        if paid:
            ingredients_required = check_resources(order)
            if ingredients_required:
                make_order(order)
