from engine.types import Character, Weapon


def combat(attacker: Character, defender: Character):
    """Do one round of combat. Use the first weapon in each character's
    inventory.
    """
    attacker_weapon = attacker.inventory[0]  # TODO check that this is a weapon. maybe in another fn?
    defender_weapon = defender.inventory[0]  # TODO as above
    #  TODO range check
    attacker_power = attacker.pwr + attacker_weapon.might
    #  TODO defense or resistance
    attacker_dmg = attacker_power - defender.dfn
    defender.cur_hp = min(attacker_dmg - defender.cur_hp, 0)
    # TODO probably a better way to do this
    if defender.cur_hp == 0:
        return
    defender_power = defender.pwr = defender_weapon.might
    # TODO defense or resistance
    defender_dmg = defender_power - attacker.dfn
    attacker.cur_hp = min(defender_dmg - attacker.cur_hp, 0)
    if attacker.cur_hp == 0:
        return
