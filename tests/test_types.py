# TODO use hypothesis for these tests!
import pytest

from engine import types


def test_char_hp_cannot_be_negative():
    with pytest.raises(ValueError):
        c = types.Character(
            name="t",
            max_hp=5,
            cur_hp=-1,
            pwr=5,
            skl=5,
            spd=5,
            dfn=5,
            res=5,
            lck=5,
            con=5,
            inventory=[],
            skills=[],
        )


def test_cur_hp_must_be_between_0_and_max_hp():
    with pytest.raises(ValueError):
        c = types.Character(
            name="t",
            max_hp=5,
            cur_hp=99999,
            pwr=5,
            skl=5,
            spd=5,
            dfn=5,
            res=5,
            lck=5,
            con=5,
            inventory=[],
            skills=[],
        )


def test_all_non_hp_attributes_must_be_nonnegative():
    with pytest.raises(ValueError):
        c = types.Character(
            name="t",
            max_hp=5,
            cur_hp=5,
            pwr=-5,
            skl=5,
            spd=5,
            dfn=5,
            res=5,
            lck=5,
            con=5,
            inventory=[],
            skills=[],
        )
