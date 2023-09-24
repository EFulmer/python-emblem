from dataclasses import dataclass, field


@dataclass(frozen=True)
class Character:
    name: str
    # TODO class

    max_hp: int
    cur_hp: int

    pwr: int
    skl: int
    spd: int
    dfn: int
    res: int
    lck: int

    con: int

    inventory: list = field(default_factory=list)

    skills: list = field(default_factory=list)

    def __post_init__(self):
        if self.cur_hp > self.max_hp:
            raise ValueError(
                f"Current HP cannot exceed max HP (got {self.cur_hp})"
            )
        if self.cur_hp < 0:
            raise ValueError(f"Current HP cannot be less than zero")
        nonnegative_stats = {'pwr', 'skl', 'spd', 'dfn', 'res', 'lck', 'con'}
        for s in nonnegative_stats:
            if getattr(self, s) < 0:
                raise ValueError(f"{s} must be >= 0")

    @property
    def avoid(self):
        return self.spd * 2 + self.lck

    @property
    def innate_hit(self):
        return self.skl * 2 + self.lck // 2

    @property
    def base_power(self):
        # TODO some rules that will have to be implemented
        # WRT inventory:
        # need to have and represent a notion of what's "equipped";
        return self.pwr + self.inventory[0].might

    @property
    def crit(self):
        # TODO rules relating to class apply here
        return self.skl // 2 + self.inventory[0].crit

    # Evade is used in this way to allow for adding supports later.
    @property
    def evade(self):
        return self.lck


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
