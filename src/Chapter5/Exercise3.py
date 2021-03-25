"""
Exercise 3

Let's consider a simple game played with a fair coin toss. A player wins $1 for
heads and loses $1.50 for tails. The game is over when the player's balance
reaches $0. Given a certain starting point specified by the user as input,
your challenge is to write a program that simulates this game. Assume there's
an unlimited cash reserve with the computer - your opponent here.
"""

import random
import time

print("How much money do you have?")
starting_sum = float(input())
count = 0
while starting_sum > 0:
    head_or_tail = random.randint(0, 1)
    count += 1
    if head_or_tail == 1:
        starting_sum -= 1.5
        print("Tails! You currently have: ")
        print(starting_sum)
    else:
        starting_sum += 1
        print("Heads! You currently have: ")
        print(starting_sum)
    time.sleep(1)

print("You lost all your money in {0} steps".format(count))
