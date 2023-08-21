import random
from typing import Tuple

from engine.types import Character, Weapon


def rng():
    return random.randint(1, 100)


# TODO: make the combat function into a Link Arena-style generator:
# alternate until one unit loses
def combat(attacker: Character, defender: Character):
    """Do one round of combat. Use the first weapon in each character's
    inventory.
    """
    attacker_weapon = attacker.inventory[0]  # TODO check that this is a weapon. maybe in another fn?
    defender_weapon = defender.inventory[0]  # TODO as above
    #  TODO range check
    attacker_power = attacker.pwr + attacker_weapon.might
    #  TODO defense or resistance
    attacker_dmg = attacker_power - defender.dfn
    defender.cur_hp = min(attacker_dmg - defender.cur_hp, 0)
    # TODO probably a better way to do this
    if defender.cur_hp == 0:
        return
    defender_power = defender.pwr = defender_weapon.might
    # TODO defense or resistance
    defender_dmg = defender_power - attacker.dfn
    attacker.cur_hp = min(defender_dmg - attacker.cur_hp, 0)
    if attacker.cur_hp == 0:
        return

def hit_rate(attacker: Character, defender: Character) -> int:
    """Return hit rate, which should be between 1 and 100.
    """
    # TODO weapon triangle
    accuracy = attacker.inventory[0].hit + attacker.skl * 2 + attacker.lck // 2
    avoid = defender.avoid
    return accuracy - avoid


def attack_hits(attacker: Character, defender: Character) -> bool:
    # GBA-style two RN "True Hit"
    roll = sum([rng(), rng()]) // 2
    return hit_rate(attacker=attacker, defender=defender) > roll


def attack(attacker: Character, defender: Character):
    if attack_hits(attacker=attacker, defender=defender):  # TODO critical hits
        attack_power = attacker.inventory[0].might + attacker.pwr - defender.dfn  # TODO res
        defender.cur_hp = min(attack_power - defender.dfn, 0)
