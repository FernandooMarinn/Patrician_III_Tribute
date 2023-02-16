import random
import Functionalities.Utilities
import Classes.Boats_and_Convoys
import time

time_to_wait = 1.5


def calculate_probability(ship_or_convoy):
    if ship_or_convoy.player.can_be_attacked:
        number = random.randint(1, 12)
        if number == 5:
            ship_or_convoy.player.turns_to_be_attacked += 5
            ship_or_convoy.player.can_be_attacked = False
            menu_battle(ship_or_convoy, ship_or_convoy.player.pirate)


def menu_battle(ship_or_convoy, pirate_captain):
    pirates = create_pirates(pirate_captain)
    if pirates.is_convoy:
        print(f"{len(pirates.boats)} pirates ships are attacking {ship_or_convoy.name}!\n"
              "1- Fight!.\n"
              "2- Go away.\n")
    else:
        print(f"A pirate boat is attacking {ship_or_convoy.name}! What do you want to do?\n"
              "1- Fight!.\n"
              "2- Go away.\n")
    option = input()
    option = Functionalities.Utilities.correct_values(1, 2, option)
    if option == 2:
        print("Using the wind, you succeed getting away from the pirates.")
    elif option == 1:
        ship_or_convoy.player.achievements.check_if_first_combat()
        choose_combat_mode(ship_or_convoy, pirates)


def choose_combat_mode(ship_or_convoy, pirates):
    if ship_or_convoy.is_convoy and pirates.is_convoy:
        result = convoy_vs_convoy(ship_or_convoy, pirates)
    elif not ship_or_convoy.is_convoy and not pirates.is_convoy:
        result = boat_vs_boat(ship_or_convoy, pirates)
    elif ship_or_convoy.is_convoy and not pirates.is_convoy:
        result = convoy_vs_boat(ship_or_convoy, pirates)
    elif not ship_or_convoy.is_convoy and pirates.is_convoy:
        result = convoy_vs_boat(pirates, ship_or_convoy)

    winner = result[0]
    treasure = result[1]
    end_of_battle(winner, treasure)


def boat_vs_boat(ally_ship, pirate_ship):
    ally_ship.set_firepower()
    pirate_ship.set_firepower()

    treasure_pirate = calculate_pirate_treasure(pirate_ship)
    treasure_player = calculate_pirate_treasure(ally_ship)
    counter = 1

    while True:
        Functionalities.Utilities.text_separation()
        if counter % 2 != 0:
            pirate_ship.health -= ally_ship.firepower
            print(f"{ally_ship.name} fires at {pirate_ship.name} and makes {ally_ship.firepower} damage!"
                  f" {pirate_ship.name} still has {pirate_ship.health} health.")
        else:
            ally_ship.health -= pirate_ship.firepower
            print(f"{pirate_ship.name} fires at {ally_ship.name} and makes {pirate_ship.firepower} damage!"
                  f" {ally_ship.name} still has {ally_ship.health} health.")
        Functionalities.Utilities.text_separation()
        time.sleep(time_to_wait)
        if ally_ship.health < 1:
            print("Unfortunately, you have lost your ship.")
            ally_ship.player.boats.remove(ally_ship)
            del ally_ship
            return pirate_ship, treasure_player
        elif pirate_ship.health < 1:
            print("You've won! Pirate ship has sunk.")
            return ally_ship, treasure_pirate
        counter += 1


def convoy_vs_boat(convoy, boat):
    convoy.set_firepower()
    boat.set_firepower()

    convoy_treasure = calculate_pirate_treasure(convoy)
    boat_treasure = calculate_pirate_treasure(boat)

    counter = 1
    while True:
        Functionalities.Utilities.text_separation()
        if counter % 2 != 0:
            single_boat_target = random.choice(convoy.boats)
            single_boat_target.health -= boat.firepower
            print(f"{boat.name} fires at {single_boat_target.name} and makes {boat.firepower} damage!"
                  f" {single_boat_target.name} still has {single_boat_target.health} health.")
            result = check_if_sunk_and_delete(convoy)
            if not result:
                print("Combat has ended.\n")
                return boat, convoy_treasure


        else:
            for convoy_boat in convoy.boats:
                boat.health -= convoy_boat.firepower
                print(f"{convoy_boat.name} fires at {boat.name} and makes {convoy_boat.firepower} damage!"
                      f" {boat.name} still has {boat.health} health.")
                result = check_if_sunk_and_delete(boat)
                if not result:
                    print("Combat has ended.\n")
                    return convoy, boat_treasure
        Functionalities.Utilities.text_separation()
        time.sleep(time_to_wait)

        counter += 1



def convoy_vs_convoy(ally_convoy, enemy_convoy):
    ally_convoy.set_firepower()
    enemy_convoy.set_firepower()

    ally_convoy_treasure = calculate_pirate_treasure(ally_convoy)
    enemy_convoy_treasure = calculate_pirate_treasure(enemy_convoy)

    while True:
        Functionalities.Utilities.text_separation()
        for ally_boat in ally_convoy.boats:
            try:
                target = random.choice(enemy_convoy.boats)
            except IndexError:
                break
            target.health -= ally_boat.firepower
            print(f"{ally_boat.name} fires at {target.name} and makes {ally_boat.firepower} damage!"
                  f" {target.name} still has {target.health} health.")
            result = check_if_sunk_and_delete(enemy_convoy)
            if not result:
                print("Combat has ended.")
                return ally_convoy, enemy_convoy_treasure

        for enemy_boat in enemy_convoy.boats:
            try:
                target = random.choice(ally_convoy.boats)
            except IndexError:
                break
            target.health -= enemy_boat.firepower
            print(f"{enemy_boat.name} fires at {target.name} and makes {enemy_boat.firepower} damage!"
                  f" {target.name} still has {target.health} health.")
            result = check_if_sunk_and_delete(ally_convoy)
            if not result:
                print("Combat has ended.")
                return enemy_convoy, ally_convoy_treasure
        Functionalities.Utilities.text_separation()
        time.sleep(time_to_wait)

def end_of_battle(winner, treasure):
    Functionalities.Utilities.text_separation()
    Functionalities.Utilities.text_separation()
    print("{} has won the battle and has recovered a treasure from the enemy. It now adds to the inventory:\n"
          "-{} skins.\n"
          "-{} tools.\n"
          "-{} beer.\n"
          "-{} wine.\n"
          "-{} cloth.\n".format(winner.name, treasure[0], treasure[1], treasure[2], treasure[3], treasure[4]))
    if winner.is_convoy:
        boat = winner.boats[0]
    else:
        boat = winner
    boat.skins += treasure[0]
    boat.tools += treasure[1]
    boat.beer += treasure[2]
    boat.wine += treasure[3]
    boat.cloth += treasure[4]



def check_if_sunk_and_delete(ship_or_convoy):
    if ship_or_convoy.is_convoy:
        for boat in ship_or_convoy.boats:
            if boat.health < 1:
                print(f"{boat.name} has sunk.")
                ship_or_convoy.boats.remove(boat)
                del boat
                return check_if_empty_convoy(ship_or_convoy)
        return True
    else:
        if ship_or_convoy.health < 1:
            print(f"{ship_or_convoy.name} has sunk.")
            ship_or_convoy.player.boats.remove(ship_or_convoy)
            del ship_or_convoy
            return False
        else:
            return True


def check_if_empty_convoy(convoy):
    if len(convoy.boats) == 0:
        print(f"{convoy.name} convoy has entirely sunk")
        convoy.player.convoys.remove(convoy)
        del convoy
        return False
    else:
        return True


def create_pirates(pirate):
    number_of_ships = random.randint(1, 3)
    if number_of_ships == 1:
        pirate_ship = create_pirate_ship(pirate)
        return pirate_ship
    else:
        pirate_convoy = create_pirate_convoy(number_of_ships, pirate)
        pirate_convoy.player = pirate
        return pirate_convoy


def create_pirate_convoy(numer_of_ships, pirate):
    pirate_boats = [create_pirate_ship(pirate) for _ in range(numer_of_ships)]
    pirate_convoy = Classes.Boats_and_Convoys.Convoy("Pirate convoy", False, pirate_boats, pirate, False)
    pirate.convoys.append(pirate_convoy)
    return pirate_convoy


def create_pirate_ship(pirate):
    health = random.randint(50, 100)
    level = 3
    sailors = random.randint(8, 40)
    captain = True
    cannon = random.randint(0, 12)
    pirate_inventory = create_pirate_inventory(sailors + cannon)
    ship = Classes.Boats_and_Convoys.Boat(health, level, pirate_inventory, sailors, captain, cannon, "Pirate ship",
                                          False, pirate)
    pirate.boats.append(ship)
    return ship


def create_pirate_inventory(load):
    total_space = 100 - load
    each_product_max = round(total_space / 5) - 1
    all_products = [random.randint(0, each_product_max) for _ in range(6)]
    return all_products


def calculate_pirate_treasure(pirate_convoy_or_ship):
    skins = 0
    tools = 0
    beer = 0
    wine = 0
    cloth = 0
    if pirate_convoy_or_ship.is_convoy:
        for boat in pirate_convoy_or_ship.boats:
            skins += boat.skins
            tools += boat.tools
            beer += boat.beer
            wine += boat.wine
            cloth += boat.cloth
    else:
        skins += pirate_convoy_or_ship.skins
        tools += pirate_convoy_or_ship.tools
        beer += pirate_convoy_or_ship.beer
        wine += pirate_convoy_or_ship.wine
        cloth += pirate_convoy_or_ship.cloth

    return skins, tools, beer, wine, cloth
