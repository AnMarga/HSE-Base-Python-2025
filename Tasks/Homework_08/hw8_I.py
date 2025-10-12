import sys
from itertools import product

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
suits = ['пик', 'треф', 'бубен', 'червей']

remove_suit = sys.stdin.read().strip()
suits = [s for s in suits if s != remove_suit]

for rank, suit in product(ranks, suits):
    print(f"{rank} {suit}")
