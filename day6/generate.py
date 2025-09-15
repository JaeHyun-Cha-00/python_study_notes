import random
import statistics
import sys

# coin = random.choice(["head", "tails"])
# print(coin)

# number = random.randint(1, 10)
# print(number)

# cards = ["jack", "queen", "king"]
# random.shuffle(cards)

# for card in cards:
#     print(card)

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello my name is", arg)