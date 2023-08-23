import logging

from engine.combat import arena
from engine.factory import iron_sword
from engine.types import Character


def sword_unit():
    return Character(
        name='Eliwood',
        max_hp=18,
        cur_hp=18,
        pwr=5,
        skl=5,
        spd=7,
        dfn=7,
        res=3,
        lck=5,
        con=7,
        inventory=[iron_sword()],
        skills=[],
    )


def axe_unit():
    return Character(
        name='Hector',
        max_hp=18,
        cur_hp=18,
        pwr=5,
        skl=5,
        spd=7,
        dfn=7,
        res=3,
        lck=5,
        con=7,
        inventory=[iron_sword()],
        skills=[],
    )

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    eliwood, hector = sword_unit(), axe_unit()
    arena(eliwood, hector)
