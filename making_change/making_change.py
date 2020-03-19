#!/usr/bin/python

import sys

def making_change(amount, denominations):
    if amount == 0:
        return 1 # only 1 way to count nothing...
    cnt = 0  # count number of ways to make change
    for i in denominations:
        if i == 1:
            cnt =+1  # only 1 way to break with all 1's
        else:
            for j in range(1, (amount // i) + 1): # for as many times as bill fits in amount
                if amount == i * j:
                    cnt += 1
                elif amount > i * j:
                    remainder = amount - i*j
                    bills = [n for n in denominations if n < i]
                    cnt += making_change(remainder, bills)
    return cnt



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")