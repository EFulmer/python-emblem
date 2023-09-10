import pytest

import engine.combat
from engine.factory import iron_sword
from engine.types import Character, Weapon


def always_hit(attacker: Character, defender: Character) -> bool:
    return True


@pytest.fixture
def sword_unit():
    return Character(
        name="Eliwood",
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
        name="Hector",
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


def test_attack(sword_unit, axe_unit, monkeypatch):
    monkeypatch.setattr(engine.combat, "attack_hits", always_hit)
    sword_unit, axe_unit = engine.combat.attack(
        attacker=sword_unit, defender=axe_unit
    )
    assert axe_unit.cur_hp < axe_unit.max_hp
