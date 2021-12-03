import time, random
from helpers import *

t = time.time()

input = mypath + "d22-input.txt"
with open(input) as f:
    boss_stats = [int(stat.split(":")[1]) for stat in f.read().split("\n")]

logging = False
log = lambda line: print(line) if logging else None

# Part 1
# Terrible solution that simulates a million battles
# Thus correct answer is not guaranteed on first try 😿
# Guess 1: 1957 - too high
# Guess 2: 1844 - too high
# Guess 3: 1824 - correct
class Character:
    def __init__(self, name, hp=0, damage=0, armor=0, mana=0) -> None:
        self.name = name
        self.stats = {"hp": hp, "damage": damage, "armor": armor, "mana": mana}
        self.alive = True
        self.manaspent = 0

    def castSpell(self, spell, opponent, queue):
        self.stats["mana"] -= spell.mana
        self.manaspent += spell.mana
        self.spellDamage(spell.damage, opponent)
        self.stats["hp"] += spell.heal
        log(
            f"  🪄  {spell.name} | cost {spell.mana} | deals {spell.damage} dmg | heals {spell.heal}"
        )
        if spell.damage > 0:
            log(f"  ⚔️  {spell.name} deals {spell.damage} damage")
        if spell.heal > 0:
            log(f"  ❤️  {spell.name} heals {spell.heal} hp")
        spell.trigger(queue)
        self.killCheck(opponent)

    def spellDamage(self, damage, opponent):
        opponent.stats["hp"] -= damage
        self.killCheck(opponent)

    def lifeSucks(self, damage):
        self.stats["hp"] -= damage
        log(f"  🦟  a deathquito deals {damage} damage to {self.name}")
        self.killCheck(self)

    def attack(self, opponent):
        dmg = max(1, self.stats["damage"] - opponent.stats["armor"])
        opponent.stats["hp"] -= dmg
        log(f"  ⚔️  {self.name} deals {dmg} damage to {opponent.name}")
        self.killCheck(opponent)

    def killCheck(self, target):
        if target.stats["hp"] <= 0:
            target.alive = False
            log(f"  💀  {target.name} was killed by {self.name}")


class Spell:
    def __init__(self, name, mana, damage=0, heal=0, effect=None) -> None:
        self.name = name
        self.mana = mana
        self.damage = damage
        self.heal = heal
        self.effect = effect

    def trigger(self, queue):
        if self.effect is not None:
            queue.append(self.effect)


class Effect:
    def __init__(self, name, turns=0, armor=0, damage=0, mana=0) -> None:
        self.name = name
        self.turns = turns
        self.armor = armor
        self.damage = damage
        self.mana = mana

    def ping(self, player, opponent):
        if self.armor != 0:
            player.stats["armor"] = self.armor
        opponent.stats["hp"] -= self.damage
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


def applyEffects(queue, player, opponent):
    new_queue = []
    for effect in queue:
        if effect.ping(player, opponent):
            new_queue.append(effect)
    return new_queue


def getAvailableSpells(player, queue):
    available = []
    effects = [effect.name for effect in queue if effect.turns > 1]
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


def fight(run_battles, level="normal"):
    spent_mana = []
    for battle in range(run_battles):
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
            if level == "hard":
                player.lifeSucks(1)
            effects_queue = applyEffects(effects_queue, player, boss)
            spells = getAvailableSpells(player, effects_queue)
            if len(spells) < 1:
                log(f"  💀  Player died because of no spells to cast")
                player.alive = False
                still_standing = False

            # Boss turn
            if player.alive and boss.alive:
                player.castSpell(getSpell(random.choice(spells)), boss, effects_queue)
                log(f"Boss turn: {boss.stats}")
                if level == "hard":
                    player.lifeSucks(1)
                effects_queue = applyEffects(effects_queue, player, boss)

            if player.alive and boss.alive:
                boss.attack(player)

            log(
                f"End of battle {battle} | round {round}\n[P]: {player.stats}\n[B]: {boss.stats}\n"
            )

            if not player.alive or not boss.alive:
                still_standing = False
                if player.alive:
                    spent_mana.append(player.manaspent)
            round += 1
    return spent_mana


mana = fight(1000000)
dropstar(43, min(mana), t)

# Part 2
# Not working on one million sims... :(
mana = fight(1000000, "hard")
dropstar(44, min(mana), t)
