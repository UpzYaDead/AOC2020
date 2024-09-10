import os

from typing import NamedTuple, List, Dict, Set, Tuple


RAW ="""mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

class Food(NamedTuple):
    ingredients: List[str]
    allergens: List[str]


mydir = 'C:\\Users\\thoma\\Documents\\Studie\\Advent of Code\\2020-2021\\data'
myfile = 'data_21'
data_21 = os.path.join(mydir, myfile)
data = []

def create_foods() -> List[Food]:
    foods: List[Food] = []
    with open(data_21,'r') as file:
        while (True):
            # read next line
            line = file.readline()
            if not line:
                break
            new_line = line.strip()
            ingredients, allergens = new_line.split("(contains ")
            allergens = allergens[:-1]
            allergens = allergens.split(",")
            ingredients = ingredients.split(" ")[:-1]
            allergens = [allergen.strip() for allergen in allergens]
            foods.append(Food(ingredients, allergens))

    return foods


def check_done(aller_to_ingr: Dict[str, Set[str]]) -> bool:
    for ingredient in aller_to_ingr.values():
        if len(ingredient) != 1:
            return False
    return True

def update(aller_to_ingr: Dict[str, Set[str]], removed: Set[str]) -> Tuple[Dict[str, Set[str]], Set[str]]:
    print("\n\n\n")
    #find the allergen that can only be in 1 ingredient
    allergen_to_not_rempove, food_to_remove =  None, None
    for allergen in aller_to_ingr.keys():
        food = aller_to_ingr[allergen]
        if len(food) == 1 and allergen not in removed:
            temp = list(food)
            food_to_remove = temp[0]
            allergen_to_not_rempove = allergen
    print("the allergen {} with the food {} ".format(allergen_to_not_rempove, food_to_remove))
    for allergen in aller_to_ingr.keys():
        if food_to_remove in aller_to_ingr[allergen] and allergen != allergen_to_not_rempove:
            print("We remove {} from {} ".format(food_to_remove,aller_to_ingr[allergen]))
            aller_to_ingr[allergen].remove(food_to_remove)
            print("After the update ",aller_to_ingr[allergen])
    print("After the first update: ",aller_to_ingr)
    removed.add(allergen_to_not_rempove)
    return aller_to_ingr, removed

def cant_contain_allergens(foods: List[Food]) -> int:
    """
    Plan, map the allergens to the possible ingredients.
    Use set intersection or something.
    Stop if all the allergens are matched to 1 food
    """
    all_ingredients = {ingredient for food in foods for ingredient in food.ingredients}
    allergen_to_ingredient = {}
    for food in foods:
        for allergen in food.allergens:
            if allergen not in allergen_to_ingredient.keys():
                allergen_to_ingredient[allergen] = set(food.ingredients)
            else:
                ingredients = set(food.ingredients)
                old_ingredients = allergen_to_ingredient[allergen]
                new_ingredients = old_ingredients.intersection(ingredients)
                allergen_to_ingredient[allergen] = new_ingredients
    print(allergen_to_ingredient)
    done = False
    removed = set()
    while not done:
        print("Allergen ingredient dict: ",allergen_to_ingredient)
        temp = update(allergen_to_ingredient, removed)
        allergen_to_ingredient, removed = temp[0], temp[1]
        done = check_done(allergen_to_ingredient)
    allergen_ingredients = {ingredient for ingredient_set in allergen_to_ingredient.values() for ingredient in ingredient_set}
    clean_ingredients = [ingredient for ingredient in all_ingredients if ingredient not in allergen_ingredients]
    print(clean_ingredients)
    clearn_ingredient_occurences = len([ingredient for food in foods for ingredient in food.ingredients if ingredient in clean_ingredients])

    #part 2

    print(sorted(allergen_to_ingredient))
    dangerous_list = [ingredient for allergen in sorted(allergen_to_ingredient) for ingredient in allergen_to_ingredient[allergen]]
    print(dangerous_list)
    dangerous_str = ""
    for ingredient in dangerous_list:
        dangerous_str += ingredient + ","
    print(dangerous_str[:-1])
    return clearn_ingredient_occurences


foods = create_foods()
print(cant_contain_allergens(foods))