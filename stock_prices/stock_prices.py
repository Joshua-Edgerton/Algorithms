#!/usr/bin/python

import argparse

def find_max_profit(prices):
    #Declare "smallest" equal to the first element in the given array
    smallest = prices[0]
    #For each index in the array
    for i in range(len(prices)):
        #if that index is less than the previously set smallest value AND that index does not equal the same value of the last element in prices
        if prices[i] < smallest and prices[i] != prices[len(prices) - 1]:
            #Then "smallest" equals that index
            smallest = prices[i]
    
    #"Smallest_value" equals the smallest index value in prices
    smallest_value_index = prices.index(smallest)
    #"shortened_prices" equals the element within prices thats just 1 higher in the array
    shortened_prices = prices[smallest_value_index + 1 :]
    largest = shortened_prices[0]

    #For each index in range of the whole "shortened_prices" array
    for i in range(len(shortened_prices)):
        #if that index is greater than "largest"
        if shortened_prices[i] > largest:
            #"largest" then equals that index
            largest = shortened_prices[i]
    #Return the largest buy minus the smallest sell
    return largest - smallest


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))