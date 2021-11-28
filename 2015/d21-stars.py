import time, itertools
from helpers import *

t = time.time()

input = mypath + "d21-input.txt"
with open(input) as f:
    boss_stats = [int(stat.split(":")[1]) for stat in f.read().split("\n")]

# Additional text file with puzzle player shop items
items = mypath + "d21-items.txt"
with open(items) as f:
    items = f.read().split("\n\n")


# Part 1
class Character:
    def __init__(self, name, hp=0, damage=0, armor=0, gold=0) -> None:
        self.name = name
        self.stats = {"hp": hp, "damage": damage, "armor": armor}
        self.items = []
        self.gold = gold
        self.spent = 0
        self.alive = True

    def addItem(self, item):
        self.items.append(item)
        self.gold -= item.cost
        self.spent += item.cost
        self.stats["damage"] += item.damage
        self.stats["armor"] += item.armor
        # print(f"{self.name} equipped {item.name}.")

    def attacks(self, opponent):
        dmg = max(1, self.stats["damage"] - opponent.stats["armor"])
        opponent.stats["hp"] -= dmg
        # print(f"{self.name} dealt {dmg} damage to {opponent.name}.")
        if opponent.stats["hp"] <= 0:
            opponent.alive = False
            # print(f"{opponent.name} was killed by {self.name}.")


class Item:
    def __init__(self, name, cost, damage, armor, type=None) -> None:
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor
        self.type = type


# Items from list of string -> list of objects
def getItems(item_string):
    items = [i.split(",") for i in item_string.split("\n")]
    items = [[int(i) if i.isdigit() else i for i in item] for item in items]
    return [Item(*i) for i in items]


def viewTracer(tracer):
    for round in range(len(tracer)):
        viewTrace(tracer, round)


def viewTrace(tracer, round):
    outcome = "Won!" if tracer[round]["playerstatus"] else "Lost"
    items = ", ".join(
        [
            "(" + t.type[0] + "-" + str(t.cost) + ") " + t.name
            for t in tracer[round]["items"]
        ]
    )
    cost = tracer[round]["gold spent"]
    ps = tracer[round]["pstats"]
    pstats = ps["hp"], ps["damage"], ps["armor"]
    bs = tracer[round]["bstats"]
    bstats = bs["hp"], bs["damage"], bs["armor"]
    print(f"{round+1} | {outcome} | H/D/A: {pstats} {bstats} | {cost} | {items}")


weapons = getItems(items[0])
armors = getItems(items[1])
rings = getItems(items[2])

# Calculate item combinations
weapon_options = [1, 2, 3, 4, 5]
w_opts = itertools.combinations(weapon_options, 1)

armor_options = [0, 1, 2, 3, 4, 5]
a_opts = itertools.combinations(armor_options, 1)

ring_options = [0, 1, 2, 3, 4, 5, 6]
r_opts = [(0, 0)] + list(itertools.combinations(ring_options, 2))

equipment = list(itertools.product(w_opts, a_opts, r_opts))
gold_init = 1000
tracer = {}

for round, equip in enumerate(equipment):
    # Reset players
    player = Character("Player", 100, 0, 0, gold_init)
    boss = Character("Boss", *boss_stats)

    # Equip player
    w, a, r = equip
    if w[0] != 0:
        player.addItem(weapons[w[0] - 1])
    if a[0] != 0:
        player.addItem(armors[a[0] - 1])
    if r[0] != 0:
        player.addItem(rings[r[0] - 1])
    if r[1] != 0:
        player.addItem(rings[r[1] - 1])

    # Fight
    while True:
        if player.alive and boss.alive:
            player.attacks(boss)
        if player.alive and boss.alive:
            boss.attacks(player)
        if not player.alive or not boss.alive:
            break

    tracer[round] = {
        "round": round,
        "playerstatus": player.alive,
        "items": player.items,
        "gold spent": player.spent,
        "pstats": player.stats,
        "bstats": boss.stats,
    }

# viewTracer(tracer)

gold_winning = [v["gold spent"] for (k, v) in tracer.items() if v["playerstatus"]]

dropstar(41, min(gold_winning), t)

# Part 2
gold_losing = [v["gold spent"] for (k, v) in tracer.items() if not v["playerstatus"]]

dropstar(42, max(gold_losing), t)
