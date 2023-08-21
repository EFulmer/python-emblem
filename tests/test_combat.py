import pytest

from engine.combat import combat
from engine.types import Character, Weapon


IRON_SWORD = Weapon(
    name='Iron Sword',
    might=5,
    hit=95,
    crit=0,
    weight=5,
    rng=(1, 1),
)


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
        inventory=[IRON_SWORD],
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
        inventory=[IRON_SWORD],
        skills=[],
    )


def test_combat(sword_unit, axe_unit):
    # TODO force a hit
    combat(attacker=sword_unit, defender=axe_unit)
    assert sword_unit.cur_hp < sword_unit.max_hp
