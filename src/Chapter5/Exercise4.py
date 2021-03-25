"""
Exercise 4

Create a list, x, consisting of the numbers [1,2,3,4]. Then, call the shuffle()
function(), passing this list as an argument. You'll see that the numbers in x
have been shuffled. Note, that the list is shiffled "in place." The is, the
original order is lost.
But what if you wanted to use this program in a card game?There, it's not
enough to simply output the shuffled list of integers. You'll also need a way
to map back the integers to the specific suit and rank of each card.
"""

import random


def initialize_deck():
    suits = ["clubs", "diamonds", "hearts", "spades"]
    ranks = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "jack",
        "queen",
        "king",
        "ace",
    ]
    return [(suit, rank) for suit in suits for rank in ranks]


def print_deck(deck):
    for card in deck:
        print("{0} of {1}".format(card[0], card[1]))


deck = initialize_deck()
print("Before shuffelig: ")
print_deck(deck)

random.shuffle(deck)
print("After shuffeling: ")
print_deck(deck)
