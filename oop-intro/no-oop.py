#!/usr/bin/env python3

import random


def role():
    player1_dice = []
    player2_dice = []
    print("=" * 70)
    for i in range(3):
        player1_dice.append(random.randint(1,6))
        player2_dice.append(random.randint(1,6))

    print("Player 1 rolled " + str(player1_dice))
    print("Player 2 rolled " + str(player2_dice))

    if sum(player1_dice) == sum(player2_dice):
        print("Draw")
    elif sum(player1_dice) > sum(player2_dice):
        print("Player 1 Wins")
    else:
        print("Player 2 Wins")


do_run = True

while do_run:
    role()
    response = input("\nDo you wish to role again? [Y/n]: ")
    if response.lower() == "n":
        do_run = False

