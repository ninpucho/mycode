#!/usr/bin/env python3

from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = []
        for i in range(3):
            self.dice.append(randint(1,6))

    def get_dice(self):
        return self.dice


def role():
    player1 = Player()
    player2 = Player()

    player1.roll()
    player2.roll()
    print("=" * 70)
    print("Player 1 rolled " + str(player1.get_dice()))
    print("Player 2 rolled " + str(player2.get_dice()))

    if sum(player1.get_dice()) == sum(player2.get_dice()):
        print("Draw")
    elif sum(player1.get_dice()) > sum(player2.get_dice()):
        print("Player 1 Wins")
    else:
        print("Player 2 Wins")


do_run = True

while do_run:
    role()
    response = input("\nDo you wish to role again? [Y/n]: ")
    if response.lower() == "n":
        do_run = False

