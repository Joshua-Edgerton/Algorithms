#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    moves = ["rock", "paper", "scissors"]
    permutations = []
    result = []

    if n == 0:
        return [[]]

    def form_permutations(arr, rounds):
        if rounds > 0:
          for move in moves:
              form_permutations(arr + [move], rounds - 1)
        else:
            result.append(arr)
            return arr


    form_permutations(permutations, n)
    return result

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')