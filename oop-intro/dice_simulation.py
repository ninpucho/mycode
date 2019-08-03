#!/usr/bin/env python3

from cheatdice import *


def main():
    swapper = Cheat_Swapper()
    loaded_dice = Cheat_Loaded_Dice()
    good_guy = Player()

    draws = 0
    swapper_score = 0
    loaded_dice_score = 0
    good_guy_score = 0

    number_of_games = input("Enter number of games to play: ")
    if not number_of_games.isnumeric():
        print("You need to enter a number!!")
    number_of_games = int(number_of_games)

    game_number = 0

    print(f"Simulation Running {number_of_games} Game(s)")
    print("=" * 50)

    while game_number < number_of_games:
        swapper.roll()
        loaded_dice.roll()
        good_guy.roll()

        swapper.cheat()
        loaded_dice.cheat()

        if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()) == sum(good_guy.get_dice()):
            draws += 1
            pass # Draw no one won...
        elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()) and sum(swapper.get_dice()) > sum(good_guy.get_dice()):
            swapper_score += 1

        elif sum(loaded_dice.get_dice()) > sum(swapper.get_dice()) and sum(loaded_dice.get_dice()) > sum(good_guy.get_dice()):
            loaded_dice_score += 1

        elif sum(swapper.get_dice()) < sum(good_guy.get_dice()) and sum(loaded_dice.get_dice()) < sum(good_guy.get_dice()):
            good_guy_score += 1

        game_number += 1

    print("Simulation Complete")
    print("-" * 50)
    print("Final Scores")
    print("*" * 50)
    print("Swapper Won: ",swapper_score)
    print("Loaded Dice: ",loaded_dice_score)
    print("Good Guy:    ",good_guy_score)
    print("Draws:       ",draws)


main()

print("exit")
