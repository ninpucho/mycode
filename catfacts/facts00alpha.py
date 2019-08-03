#!/usr/bin/env python3

import requests
import random
def part01():

    r = requests.get("https://cat-fact.herokuapp.com/facts")

    print(dir(r))

def part02():

    r = requests.get("https://cat-fact.herokuapp.com/facts")

    print(r.json())

def part03():
    print("Gathering data, please wait")
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    #for catfact in r.json()["all"]:
    #    print(catfact.get("text"))
    do_run = True
    while do_run:
        random_fact = random.choice(r.json()["all"])
        print("=" * 50,"\n")
        print(random_fact["text"].ljust(50))
        print(f"Submitted By: {random_fact['user']['name']['first']} {random_fact['user']['name']['last']}")
        print("\n" + ("=" * 50))
        response = input("\nDo you wish to run again? [Y/n]: ")
        if response.lower() == "n":
            do_run = False
#    print(f"Information provided by{r.url()}")

part03()
