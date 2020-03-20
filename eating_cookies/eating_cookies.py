#!/usr/bin/python
#Initial commit change
import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

#changed cache to default to an empty object
def eating_cookies(n, cache={}):
  #if the amount of cookies equals 0, then return 1
  if n == 0:
      return 1
  #else if the amount of cookies is 1 or 2, return that number
  elif n <= 2:
      return n
  #else if the amount of cookies is within cache, return the index in cache
  elif n in cache:
      return cache[n]

  #else "value" equals "eating_cookies" with a param of n-3 + n-2 + n-1
  value = eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)
  #The cache of this index will equal that value
  cache[n] = value
  #return the "value" to represent different ways to eat a different amount of cookies
  return value

print(eating_cookies(5), 13)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')