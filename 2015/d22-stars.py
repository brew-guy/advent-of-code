import time, random
from helpers import *

t = time.time()

input = mypath + "d22-input.txt"
with open(input) as f:
    boss_stats = [int(stat.split(":")[1]) for stat in f.read().split("\n")]

logging = False
log = lambda line: print(line) if logging else None

# Part 1
class Character:
    def __init__(self, name, hp=0, damage=0, armor=0, mana=0) -> None:
        self.name = name
        self.stats = {"hp": hp, "damage": damage, "armor": armor, "mana": mana}
        self.alive = True
        self.manaspent = 0

    def castSpell(self, spell):
        self.stats["mana"] -= spell.mana
        self.manaspent += spell.mana
        boss.stats["hp"] -= spell.damage
        self.stats["hp"] += spell.heal
        log(
            f"  🪄  {spell.name} | cost {spell.mana} | deals {spell.damage} dmg | heals {spell.heal}"
        )
        if spell.damage > 0:
            log(f"  ⚔️  {spell.name} deals {spell.damage} damage")
        if spell.heal > 0:
            log(f"  ❤️  {spell.name} heals {spell.heal} hp")
        spell.trigger()

    def attack(self, opponent):
        dmg = max(1, self.stats["damage"] - opponent.stats["armor"])
        opponent.stats["hp"] -= dmg
        log(f"  ⚔️  {self.name} deals {dmg} damage to {opponent.name}")
        if opponent.stats["hp"] <= 0:
            opponent.alive = False
            log(f"  💀  {opponent.name} was killed by {self.name}")


class Spell:
    def __init__(self, name, mana, damage=0, heal=0, effect=None) -> None:
        self.name = name
        self.mana = mana
        self.damage = damage
        self.heal = heal
        self.effect = effect

    def trigger(self):
        if self.effect is not None:
            effects_queue.append(self.effect)


class Effect:
    def __init__(self, name, turns=0, armor=0, damage=0, mana=0) -> None:
        self.name = name
        self.turns = turns
        self.armor = armor
        self.damage = damage
        self.mana = mana

    def ping(self):
        # For crying out loud this part sucks!
        if self.armor != 0:
            player.stats["armor"] = self.armor
        boss.stats["hp"] -= self.damage
        player.stats["mana"] += self.mana
        self.turns -= 1
        if self.turns < 1:
            player.stats["armor"] -= self.armor
            log(f"  🍃 {self.name} wears off")
            return False
        else:
            log(f"  ⏱️  {self.name} is active for {self.turns} more turns")
            return True


def getSpell(name):
    if name == "Magic Missile":
        return Spell("Magic Missile", 53, 4)
    if name == "Drain":
        return Spell("Drain", 73, 2, 2)
    if name == "Shield":
        return Spell("Shield", 113, 0, 0, Effect("shield", 6, 7))
    if name == "Poison":
        return Spell("Poison", 173, 0, 0, Effect("poison", 6, 0, 3))
    if name == "Recharge":
        return Spell("Recharge", 229, 0, 0, Effect("recharge", 5, 0, 0, 101))


def applyEffects(queue):
    new_queue = []
    for effect in queue:
        if effect.ping():
            new_queue.append(effect)
    return new_queue


def getAvailableSpells():
    available = []
    effects = [effect.name for effect in effects_queue if effect.turns > 1]
    for spell in spellbook:
        if (
            spellbook[spell]["mana"] < player.stats["mana"]
            and spellbook[spell]["effect"] not in effects
        ):
            available.append(spell)
    return available


spellbook = {
    "Magic Missile": {"mana": 53, "effect": ""},
    "Drain": {"mana": 73, "effect": ""},
    "Shield": {"mana": 113, "effect": "shield"},
    "Poison": {"mana": 173, "effect": "poison"},
    "Recharge": {"mana": 229, "effect": "recharge"},
}

spent_mana = []
best_case = []

for battle in range(10):
    # Initiate battle
    player = Character("Player", 50, 0, 0, 500)
    boss = Character("Boss", *boss_stats)
    effects_queue = []
    round = 1
    still_standing = True

    # Fight
    while still_standing:

        # Player turn
        log(f"Player turn: {player.stats}")
        effects_queue = applyEffects(effects_queue)
        spells = getAvailableSpells()
        if len(spells) < 1:
            log(f"  💀  Player died because of no spells to cast")
            still_standing = False
            continue

        if player.alive and boss.alive:
            player.castSpell(getSpell(random.choice(spells)))

        # Boss turn
        log(f"Boss turn: {boss.stats}")
        effects_queue = applyEffects(effects_queue)

        if player.alive and boss.alive:
            boss.attack(player)

        log(f"End of round {round}\n[P]: {player.stats}\n[B]: {boss.stats}\n")

        print(player.alive, boss.alive)

        if not player.alive or not boss.alive:
            still_standing = False
            if player.alive:
                spent_mana.append(player.manaspent)
            best_case.append((player.stats["hp"], boss.stats["hp"]))
        round += 1

print(spent_mana)
print(sorted(best_case))
# dropstar(43, , t)

# Part 2

# dropstar(44, , t)
