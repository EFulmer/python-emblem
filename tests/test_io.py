# TODO make fixtures module
from engine.utils import character_from_yaml, character_to_yaml
from tests.test_combat import axe_unit, sword_unit


def test_character_to_yaml(tmp_path, axe_unit):
    path = tmp_path / "test_char.yaml"
    character_to_yaml(character=axe_unit, file_name=path)


def test_character_yaml_roundtrip(tmp_path, axe_unit):
    path = tmp_path / "test_char.yaml"
    character_to_yaml(axe_unit, path)
    actual = character_from_yaml(path)
    assert axe_unit == actual
