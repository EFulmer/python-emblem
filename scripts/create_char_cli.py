from pathlib import Path

import click

from engine.types import Character
from engine.utils import character_to_yaml


@click.command()
@click.option("--name", required=True, type=str)
@click.option("--hp", required=True, type=int)
@click.option("--pwr", required=True, type=int)
@click.option("--skl", required=True, type=int)
@click.option("--spd", required=True, type=int)
@click.option("--dfn", required=True, type=int)
@click.option("--res", required=True, type=int)
@click.option("--lck", required=True, type=int)
@click.option("--con", required=True, type=int)
@click.option("--fname", required=True, type=Path)
def main(
    name: str,
    hp: int,
    pwr: int,
    skl: int,
    spd: int,
    dfn: int,
    res: int,
    lck: int,
    con: int,
    fname: Path,
):
    character = Character(
        name=name,
        cur_hp=hp,
        max_hp=hp,
        pwr=pwr,
        skl=skl,
        spd=spd,
        dfn=dfn,
        res=res,
        lck=lck,
        con=con,
    )
    character_to_yaml(character, fname)


if __name__ == "__main__":
    main()
