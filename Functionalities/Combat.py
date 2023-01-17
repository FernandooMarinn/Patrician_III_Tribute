import random
def boat_battle_who_starts(boat, pirate):
    who_starts = random.choice([boat, pirate])
    who_goes_after = 0
    if who_starts == boat:
        who_goes_after = pirate
    else:
        who_goes_after = boat
    return who_starts, who_goes_after


def boat_battle(who_starts, who_goes_after):
    while who_starts.health > 0 or who_goes_after.health > 0:
        who_goes_after.health -= who_starts.firepower
        print("{} fires at {} and made {} damage."
              .format(who_starts.name, who_goes_after.name, who_starts.firepower))
        who_starts.health -= who_goes_after.firepower
        print("{} fires at {} and made {} damage."
              .format(who_goes_after.name, who_starts.name, who_goes_after.firepower))
        print("{} health is {} and {} health is {}."
              .format(who_starts.name, who_starts.health, who_goes_after.name, who_goes_after.health))