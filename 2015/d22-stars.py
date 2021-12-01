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
# Generér en effects queue som afspiller effects i starten af hver tur.
# Hvis en effekt stopper, skal den fjernes fra queue, så f.eks. samme spell
# kan kastes og trigge samme effekt i samme tur som en effekt ophører


class Character:
    def __init__(self, name, hp=0, damage=0, armor=0, mana=0) -> None:
        self.name = name
        self.stats = {"hp": hp, "damage": damage, "armor": armor, "mana": mana}
        self.items = []
        self.spells = []
        self.effects = []
        self.gold = 0
        self.alive = True

    def addItem(self, item):
        self.items.append(item)
        self.gold -= item.cost
        self.stats["damage"] += item.damage
        self.stats["armor"] += item.armor
        # print(f"{self.name} equipped {item.name}.")

    def addSpell(self, spell):
        self.spells.append(spell)
        # print(f"{self.name} equipped {spell.name}.")

    def castSpell(self, spell):
        self.stats["mana"] -= spell.mana
        pass

    def attack(self, opponent):
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


class Spell:
    def __init__(self, name, mana, damage=0, heal=0, effect=0, type=None) -> None:
        self.name = name
        self.mana = mana
        self.damage = damage
        self.heal = heal
        self.type = "Spell"


class Effect:
    def __init__(self, turns, armor, damage, mana) -> None:
        self.turns = turns
        self.armor = armor
        self.damage = damage
        self.mana = mana

    def ping(self):
        # apply effects and count down turns counter on ping
        # then wear off effect if turn = 0
        pass


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

# Initiate an effects queue
effects_queue = []

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
    # Apply active effects from trigger queue
    # <insert effect.ping() here>
    while True:
        if player.alive and boss.alive:
            player.attack(boss)
        if player.alive and boss.alive:
            boss.attack(player)
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
