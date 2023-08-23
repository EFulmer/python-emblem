from dataclasses import replace
import logging
import random
from typing import Tuple

from engine.types import Character, Weapon


def rng():
    return random.randint(1, 100)

def hit_rate(attacker: Character, defender: Character) -> int:
    """Return hit rate, which should be between 1 and 100.
    """
    # TODO weapon triangle
    accuracy = attacker.inventory[0].hit + attacker.skl * 2 + attacker.lck // 2
    avoid = defender.avoid
    return min(100, max(accuracy - avoid, 0))


def attack_hits(attacker: Character, defender: Character) -> bool:
    # GBA-style two RN "True Hit"
    roll = sum([rng(), rng()]) // 2
    return hit_rate(attacker=attacker, defender=defender) > roll


def attack(attacker: Character, defender: Character) -> Tuple[Character, Character]:
    """Run one attack, checking for whether it hits first.

    Args:
        attacker: The character making the attack.
        defener: The character being attacked.

    Returns:
        2-tuple of the updated attacker and defender, in that order.
    """
    if attack_hits(attacker=attacker, defender=defender):  # TODO critical hits
        attack_power = attacker.inventory[0].might + attacker.pwr - defender.dfn  # TODO res
        new_defender_hp = max(defender.cur_hp - attack_power - defender.dfn, 0)
        # TODO durability
        return (attacker, replace(defender, cur_hp=new_defender_hp))
    else:
        return (attacker, defender)


def combat_summary(c1: Character, c2: Character):
    pass


def arena(c1: Character, c2: Character):
    """Do 'arena' style combat between the two characters, until one's
    HP hits 0.

    Args:
        c1: The first character to attack.
        c2: The second character to attack.
    """
    while c1.cur_hp > 0 or c2.cur_hp > 0:
        logging.info(f"{c1.name} attacks!")
        c1, c2 = attack(c1, c2)
        logging.info(f"{c2.cur_hp = }")
        logging.info(f"{c2.name} attacks!")
        c2, c1 = attack(c2, c1)
        logging.info(f"{c1.cur_hp = }")
