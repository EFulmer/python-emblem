import dataclasses
import pathlib

import yaml

import engine.types


def character_to_yaml(
    character: engine.types.Character, file_name: pathlib.Path
):
    with open(file_name, "w") as f:
        f.write(yaml.dump(dataclasses.asdict(character)))


def character_from_yaml(file_name: pathlib.Path) -> engine.types.Character:
    with open(file_name, "r") as f:
        data = yaml.load(f, yaml.CLoader)
    character = engine.types.Character(**data)
    # TODO find & use a more elegant way to deserialize nested objects
    new_inventory = [engine.types.Weapon(**i) for i in character.inventory]
    character = dataclasses.replace(character, inventory=new_inventory)
    return character
