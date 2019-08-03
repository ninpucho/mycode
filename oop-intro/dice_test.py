#!/usr/bin/env python3

from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice

def role():
    cheater1 = Cheat_Swapper()
    cheater2 = Cheat_Loaded_Dice()

    cheater1.roll()
    cheater2.roll()
    print("=" * 70)
    print("Player 1 rolled " + str(cheater1.get_dice()), sum(cheater1.get_dice()))
    print("Player 2 rolled " + str(cheater2.get_dice()), sum(cheater2.get_dice()))


    cheater1.cheat()
    cheater2.cheat()
    print("=" * 70)
    print("Player 1 rolled " + str(cheater1.get_dice()), sum(cheater1.get_dice()))
    print("Player 2 rolled " + str(cheater2.get_dice()), sum(cheater2.get_dice()))

    if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
        print("Draw")
    elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
        print("Player 1 Wins")
    else:
        print("Player 2 Wins")


do_run = True

while do_run:
    role()
    response = input("\nDo you wish to role again? [Y/n]: ")
    if response.lower() == "n":
        do_run = False

