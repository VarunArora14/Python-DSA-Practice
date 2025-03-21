from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available_supplies = set(supplies)

        recipe_to_ingredients = {recipes[i]: ingredients[i] for i in range(len(recipes))}

        visited = {}
        result = []

        def can_make(recipe):
            # circular dependency resolution (same recipe1 comes as ingredient in other recipe2 where recipe2 was ingredient in recipe1)
            if recipe in visited and visited[recipe] == 0:
                return False

            if recipe in available_supplies:
                return True

            # recipe not in supplies or existing recipes (this was an ingredient but how to make it is not there)
            if recipe not in recipe_to_ingredients:
                return False

            # start finding the ingredients of this recipe
            visited[recipe] = 0

            for ingredient in recipe_to_ingredients[recipe]:
                if not can_make(ingredient):
                    visited[recipe] = -1
                    return False

            visited[recipe] = 1
            available_supplies.add(recipe)  # created recipe acts as supply
            result.append(recipe)
            return True

        for recipe in recipes:
            can_make(recipe)

        return [recipe for recipe in recipes if recipe in visited and visited[recipe] == 1]


recipes = ["bread", "sandwich"]
ingredients = [["yeast", "flour"], ["bread", "meat"]]

supplies = ["yeast", "flour", "meat"]
s = Solution()
print(s.findAllRecipes(ingredients=ingredients, recipes=recipes, supplies=supplies))


"""
This is a dependency solving problem. We have supplies which can be used as ingredients, and for all other recipes, we check if those ingredients exist, if not
then whether they can be created before or not.

We go through each recipe and for each recipe we save 3 states - 0,1,-1

0 - currently visiting
1 - recipe can be created
-1 - recipe cannot be created

if recipe does not exist in visited then we mark it as 0 first and then traverse

after visiting, we go through it's ingredients and if their visited is 1 then fine, otherwise 
- if recipe is visited with 0 value then it means circular dependency is there so return False as it cannot be resolves (flour->wheat and wheat->flour as example)
- if recipe in supplies then return true
- if recipe does not exist in recipe list return False (this was an ingredient, where we tried to find it's recipe but it was not there)

Now, mark the current recipe as 0 to start finding it's ingredients and for each ingredient run the same method. If any return False then return False

If it can be created, then add recipe to results and mark the recipe in supplies.
"""
