# Rock Paper Scissor

import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
playerchoice = input(
    "Enter...\n1 for Rock, \n2 for Paper, \n3 for Scissors: \n\n"
)  # input always returns a string
player = int(playerchoice)  # Casting to an int
if player < 1 or player > 3:
    sys.exit("You must enter 1,2, or 3.")


computerchoice = random.choice("123")
computer = int(computerchoice)
print(" ")

print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

if player == computer:
    print("It's a tie! 😯")
elif player == 1 and computer == 2:
    print("You lose! 😢")
elif player == 2 and computer == 3:
    print("You lose! 😢")
elif player == 3 and computer == 1:
    print("You lose! 😢")
else:
    print("You win! 🥳")
