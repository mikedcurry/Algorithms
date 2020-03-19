#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    m = [['rock'], ['paper'], ['scissors']]
    l = []
    #base-case n <= 1
    if n <= 0:
        return [[]]
    elif n == 1:
        return m
    #recursion: append each member of n-1 to each member of m until n-1 = 1
    for i in m:
        for p in rock_paper_scissors(n-1):
            l.append(i + p)
    return l


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')