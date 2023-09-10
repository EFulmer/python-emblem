"""Factories for weapons and generic units."""
from engine.types import Weapon


def iron_sword():
    return Weapon(
        name="Iron Sword",
        might=5,
        max_durability=46,
        hit=95,
        crit=0,
        weight=5,
        rng=(1, 1),
        cur_durability=46,
    )
