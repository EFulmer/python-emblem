from dataclasses import dataclass


@dataclass(frozen=True)
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

    @property
    def avoid(self):
        return self.spd * 2 + self.lck

    @property
    def innate_hit(self):
        return self.skl * 2 + self.lck // 2


@dataclass
class Weapon:
    name: str
    # TODO weapon type

    might: int
    max_durability: int
    hit: int
    crit: int
    weight: int
    rng: tuple

    cur_durability: int
