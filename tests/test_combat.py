import random

import pytest

from engine.combat import attack, combat
from engine.factory import iron_sword
from engine.types import Character, Weapon


@pytest.fixture
def rng():
    random.seed(1)


@pytest.fixture
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


@pytest.fixture
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


def test_attack(sword_unit, axe_unit, rng):
    attack(attacker=sword_unit, defender=axe_unit)
    assert axe_unit.cur_hp < axe_unit.max_hp
