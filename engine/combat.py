from dataclasses import replace
import logging
import random
from typing import Dict, Tuple

from engine.types import Character, Weapon


def rng():
    return random.randint(1, 100)


def hit_rate(attacker: Character, defender: Character) -> int:
    """Return hit rate, which should be between 1 and 100."""
    # TODO weapon triangle
    accuracy = attacker.inventory[0].hit + attacker.skl * 2 + attacker.lck // 2
    avoid = defender.avoid
    return min(100, max(accuracy - avoid, 0))


def attack_hits(attacker: Character, defender: Character) -> bool:
    # GBA-style two RN "True Hit"
    roll = sum([rng(), rng()]) // 2
    return hit_rate(attacker=attacker, defender=defender) > roll


def attack(
    attacker: Character, defender: Character
) -> Tuple[Character, Character]:
    """Run one attack, checking for whether it hits first.

    Args:
        attacker: The character making the attack.
        defener: The character being attacked.

    Returns:
        2-tuple of the updated attacker and defender, in that order.
    """
    if attack_hits(attacker=attacker, defender=defender):  # TODO critical hits
        attack_power = (
            attacker.inventory[0].might + attacker.pwr - defender.dfn
        )  # TODO res
        new_defender_hp = max(defender.cur_hp - attack_power - defender.dfn, 0)
        # TODO durability
        return (attacker, replace(defender, cur_hp=new_defender_hp))
    else:
        return (attacker, defender)


def forecast(c1: Character, c2: Character) -> Tuple[Dict, Dict]:
    """Return a combat forecast summarizing how c1 and c2 fare against
    each other.

    Has each character's current/max HP, attack, hit, crit.
    """
    c1_summary, c2_summary = {}, {}
    c1_summary["hp"] = c1.cur_hp
    c2_summary["hp"] = c2.cur_hp

    # Checking that each character can attack.
    # This will need to become more elegant when I add e.g. range.
    if c1.inventory:
        # TODO character base power function
        # TODO def/res split
        c1_summary["mt"] = c1.pwr + c1.inventory[0].might - c2.dfn
        c1_summary["hit"] = hit_rate(attacker=c1, defender=c2)
        c1_summary["crit"] = (c1.skl // 2) + c1.inventory[0].crit - c2.evade
    else:
        c1_summary["mt"] = None
        c1_summary["hit"] = None
        c1_summary["crit"] = None

    if c2.inventory:
        c2_summary["mt"] = c2.pwr + c2.inventory[0].might - c1.dfn
        c2_summary["hit"] = hit_rate(attacker=c2, defender=c1)
        c2_summary["crit"] = (c2.skl // 2) + c2.inventory[0].crit - c1.evade
    else:
        c2_summary["mt"] = None
        c2_summary["hit"] = None
        c2_summary["crit"] = None

    return c1_summary, c2_summary


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
