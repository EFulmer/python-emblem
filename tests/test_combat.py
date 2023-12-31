# TODO: clean these tests up;
# much of the setup is repeated and the assertions are brittle and basic
import pytest

import engine.combat
from engine.factory import iron_sword
from engine.types import Character, Weapon


def always_hit(attacker: Character, defender: Character) -> bool:
    return True


def never_crit(*args) -> bool:
    return 1


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
    """Basic test of attack function:
    While forcing an attack to always hit, assert that after the
    attack, the defender's HP is less than it was before combat.
    """
    monkeypatch.setattr(engine.combat, "attack_hits", always_hit)
    sword_unit, axe_unit = engine.combat.attack(
        attacker=sword_unit, defender=axe_unit
    )
    assert axe_unit.cur_hp < axe_unit.max_hp


def test_combat(sword_unit, axe_unit, monkeypatch):
    """Basic test of combat function:
    Force both attacks to always hit, and assert that both participants
    have lost HP.
    """
    monkeypatch.setattr(engine.combat, "attack_hits", always_hit)
    sword_unit, axe_unit = engine.combat.combat(
        attacker=sword_unit,
        defender=axe_unit,
    )
    # sanity check on parameter ordering
    assert sword_unit.name == "Eliwood"
    assert axe_unit.name == "Hector"
    assert axe_unit.cur_hp < axe_unit.max_hp
    assert sword_unit.cur_hp < sword_unit.max_hp


def test_arena(sword_unit, axe_unit, monkeypatch):
    monkeypatch.setattr(engine.combat, "attack_hits", always_hit)
    gi = engine.combat.arena(attacker=sword_unit, defender=axe_unit)
    sword_unit, axe_unit = next(gi)
    # sanity check on parameter ordering
    assert sword_unit.name == "Eliwood"
    assert axe_unit.name == "Hector"
    assert axe_unit.cur_hp < axe_unit.max_hp
    assert sword_unit.cur_hp < sword_unit.max_hp


def test_forecast(sword_unit, axe_unit):
    """Basic test of combat forecast.
    Since the actual numbers aren't important here we simply test
    that all the proper keys exist in the combat forecast.

    This could be made nicer in the future!
    """
    KEYS = (
        "hp",
        "mt",
        "hit",
        "crit",
    )
    cs1, cs2 = engine.combat.forecast(sword_unit, axe_unit)
    for key in KEYS:
        assert key in cs1
        assert isinstance(cs1[key], int)
        assert key in cs2
        assert isinstance(cs2[key], int)
