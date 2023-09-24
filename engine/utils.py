import dataclasses
import pathlib

import yaml

import engine.types


def character_to_yaml(character: engine.types.Character, file_name: pathlib.Path):
    with open(file_name, 'w') as f:
        f.write(yaml.dump(dataclasses.asdict(character)))
