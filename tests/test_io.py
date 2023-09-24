# TODO make fixtures module
from engine.utils import character_to_yaml
from tests.test_combat import axe_unit, sword_unit

def test_character_to_yaml(tmp_path, axe_unit):
    path = tmp_path / 'test_char.yaml'
    character_to_yaml(character=axe_unit, file_name=path)

def test_character_yaml_roundtrip():
    pass
