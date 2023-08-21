from dataclasses import dataclass


@dataclass
class Character:
    name: str

    max_hp: int
    cur_hp: int

    pwr: int
    skl: int
    spd: int
    dfn: int
    res: int
    lck: int

    con: int

    inventory: list

    skills: list


@dataclass
class Weapon:
    name: str
    # TODO weapon type

    might: int
    hit: int
    crit: int
    weight: int
    rng: tuple
