#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # initialize a variable to hold our lowest qty obtainable
    min_qty = 0
    # initialize a variable to check for first run
    first_iter = False
    # start iteration
    for i in recipe.keys():
        # Edge Case: if no matching ingredient, return 0
        if i not in ingredients:
            return 0
        else:
            # determine how many recipe qtys are in the corresponding ingredient qtys
            qty = int(ingredients[i]/recipe[i])
            if first_iter == False and qty > 0:
                # this code block runs only once
                min_qty = qty
                first_iter = not first_iter
            if qty < min_qty:
                min_qty = qty

    return min_qty


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
