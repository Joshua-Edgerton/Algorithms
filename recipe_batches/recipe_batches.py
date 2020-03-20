#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  #Set an empty array
  values = []
  #For every index in the given dictionary of recipes
  for i in recipe:
        #if that index doesnt exist within ingredients
        if i not in ingredients:
              #return 0
              return 0
        #Otherwise if it does exist
        else:
            print("ingredient amount:", ingredients[i], "\nrecipe amount:", recipe[i])
            #Append a single value of ingredients divided by recipe
            values.append(ingredients[i] // recipe[i])
            #Prints values being appended
            print("divided value:",values)

  #"smallest" = the first element in vlaues
  smallest = values[0]
  #For every index in values
  for i in range(len(values)):
      #if that index is less than "smallest" (0)
      if values[i] < smallest:
          #Then the "smallest" now equals that value
          smallest = values[i]
          
  #Outputs amount of batches that can be made with given ingredients compared to recipe
  return smallest

  # Overview:
  # Divides amount of ingredients available by the amount of ingredients needed
  # Using those numbers, returns the smallest number in that array
  # That number represents amount of batches possible

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 50, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))