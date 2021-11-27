import time, re, itertools
from helpers import *

t = time.time()

input = "d15-input.txt"
with open(input) as f:
    ingredients = f.readlines()

# Part 1
def getIngredientStats(ingredient):
    regexp = r"([A-Za-z]*): capacity (-?[0-9]*), durability (-?[0-9]*), flavor (-?[0-9]*), texture (-?[0-9]*), calories (-?[0-9]*)"
    match = re.match(regexp, ingredient)
    i, prop1, prop2, prop3, prop4, prop5 = match.groups()
    return i, int(prop1), int(prop2), int(prop3), int(prop4), int(prop5)


class Cookie:
    def __init__(self) -> None:
        self.ingredients = []

    def add(self, *ingredient):
        if isinstance(ingredient, tuple):
            self.ingredients.extend(ingredient)
        else:
            self.ingredients.append(ingredient)

    def clear(self):
        self.ingredients = []

    def isValidCookie(self):
        return sum([i.amount for i in self.ingredients]) == 100

    def calories(self):
        cal_score = max(0, sum([i.calories * i.amount for i in self.ingredients]))
        return cal_score

    def score(self):
        cap_score = max(0, sum([i.capacity * i.amount for i in self.ingredients]))
        dur_score = max(0, sum([i.durability * i.amount for i in self.ingredients]))
        fla_score = max(0, sum([i.flavor * i.amount for i in self.ingredients]))
        tex_score = max(0, sum([i.texture * i.amount for i in self.ingredients]))
        return cap_score * dur_score * fla_score * tex_score


class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories) -> None:
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories
        self.amount = 0

    def set(self, teaspoons):
        self.amount = teaspoons


objs = [Ingredient(*getIngredientStats(ingredient)) for ingredient in ingredients]
cookie = Cookie()
frosting, candy, butterscotch, sugar = objs

# Time-consuming! Permutations of all 161664 possible blend amounts
blends = [x for x in itertools.permutations(range(101), 4) if sum(x) == 100]

# May the best cookie win!
best_score = 0
for blend in blends:
    f, c, b, s = blend
    cookie.clear()

    frosting.set(f)
    candy.set(c)
    butterscotch.set(b)
    sugar.set(s)

    cookie.add(frosting, candy, butterscotch, sugar)

    score = cookie.score()
    best_score = score if score > best_score else best_score

dropstar(29, best_score, t)

# Part 2

best_score = 0
for blend in blends:
    f, c, b, s = blend
    cookie.clear()

    frosting.set(f)
    candy.set(c)
    butterscotch.set(b)
    sugar.set(s)

    cookie.add(frosting, candy, butterscotch, sugar)

    score = cookie.score()
    calories = cookie.calories()
    best_score = score if calories == 500 and score > best_score else best_score

dropstar(30, best_score, t)
