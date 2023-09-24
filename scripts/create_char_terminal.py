#!/usr/bin/env python
import rich
from rich.prompt import Prompt, IntPrompt

from engine.types import Character
from engine.utils import character_to_yaml


def main():
    name = Prompt.ask("Character name")
    hp = IntPrompt.ask("Max HP")
    pwr = IntPrompt.ask("Str/Mag")
    skl = IntPrompt.ask("Skill")
    spd = IntPrompt.ask("Speed")
    dfn = IntPrompt.ask("Defense")
    res = IntPrompt.ask("Resistance")
    lck = IntPrompt.ask("Luck")
    con = IntPrompt.ask("Constitution")

    char = Character(name=name, max_hp=hp, cur_hp=hp, pwr=pwr, skl=skl, spd=spd, dfn=dfn, res=res, lck=lck, con=con)
    rich.print(char)

    character_to_yaml(character=char, file_name=name)


if __name__ == "__main__":
    main()
