import Classes.Tavern, Classes.Shipyard, Classes.Player, Classes.Money_Lender, Classes.Cities
import random


# For check every value, in order to avoid errors.

def correct_values_number(start, final, number_to_check):
    try:
        if start <= int(number_to_check) <= final:
            return number_to_check
        else:
            while not start <= number_to_check <= final:
                print("You have written an incorrect value, your options goes from {} to {}".format(start, final))
                number_to_check = int(input())
            return number_to_check
    except ValueError:
        return False
    except TypeError:
        return False


def correct_values(start, final, number_to_check):
    """
        Avoid Value and Type errors, as well as out of range errors.
        :param start:
        :param final:
        :param number_to_check:
        :return:
        """
    is_a_number = correct_values_number(start, final, number_to_check)
    if is_a_number is False:
        print("You have to write a number\n")
        while is_a_number is False:
            number_to_check = input("Introduce a value from {} to {}.\n".format(start, final))
            is_a_number = correct_values_number(start, final, number_to_check)
        return int(is_a_number)
    else:
        return int(is_a_number)


def check_if_affordable(price, quantity, money):
    if price * quantity <= money:
        return True
    else:
        return False


def how_many_can_afford(price, money):
    can_afford_number = round(money / price)
    print("You can afford {}".format(can_afford_number))


def ask_initial_money():
    print("How much money do you wnat to start with?\n"
          "1- 5000 (very few).\n"
          "2- 10000 (few).\n"
          "3- 20000 (normal).\n"
          "4- 50000 (too much).\n")
    option = input("\n")
    option = correct_values(1, 4, option)
    money = {1: 5000, 2: 10_000, 3: 20_000, 4: 50_000}
    return money[option]


def ask_initial_city(cities):
    for i in range(len(cities)):
        print("{}- {}.".format(i + 1, cities[i].name))
    option = input("Wich city do you choose as your birthplace?\n\n")
    option = correct_values(1, len(cities), option)
    return cities[option - 1]


def create_player():
    """
    returns object player
    :return:
    """
    name = input("What is your name?\n")
    coins = ask_initial_money()
    player = Classes.Player.Player(name, coins)
    return player


def create_cities(player):
    # Puta mierda
                                #  nombre   consumption    initial            production       can_pruduce
    Lubeck = Classes.Cities.City("Lubeck", 3, 4, 6, 3, 3, 40, 60, 40, 50, 30, 0, 15, 0, 9, 0, False, True, False, True,
                                 False, False, 1, player)
    Rostock = Classes.Cities.City("Rostock", 3, 4, 6, 3, 3, 40, 40, 40, 50, 30, 0, 0, 0, 0, 0, False, False, False, False,
                                 False, False, 1, player)
    Malmo = Classes.Cities.City("Malmo", 3, 4, 6, 3, 3, 60, 60, 30, 30, 50, 8, 0, 0, 0, 7, True, False, False, False,
                                 True, False, 1, player)
    Stettin = Classes.Cities.City("Stettin", 3, 4, 6, 3, 3, 40, 50, 70, 50, 30, 0, 0, 15, 0, 0, False, False, True, True,
                                 False, False, 1, player)
    Gdanks = Classes.Cities.City("Gdanks", 3, 4, 4, 3, 3, 30, 40, 60, 40, 40, 0, 0, 10, 0, 0, False, False, True, False,
                                 False, False, 1, player)

    return Lubeck, Rostock, Malmo, Stettin, Gdanks


def add_all_buildings(cities):
    cities = create_taverns(cities)
    cities = create_shipyards(cities)
    return cities

def create_taverns(cities):
    cities_with_tavern = []
    for city in cities:
        tavern = Classes.Tavern.Tavern(city)
        city.tavern = tavern
        cities_with_tavern.append(city)
    return cities_with_tavern

def create_shipyards(cities):
    cities_with_shipyard = []
    for city in cities:
        shipyard = Classes.Shipyard.Shipyard(city)
        city.shipyard = shipyard
        cities_with_shipyard.append(city)
    return cities_with_shipyard

def calculate_list_mean(list):
    if sum(list) == 0:
        return 0
    else:
        mean = round(sum(list) / len(list))
        return mean

def calculate_average_price(old_price, old_items, new_price, new_items):
    # Calculate the average price of the old and new items
    if old_price == 0:
        return new_price
    elif new_items == 0:
        return old_price
    else:
        old_items_average_price = old_price * old_items
        new_items_average_price = new_price * new_items

        # Calculate the final average price
        average_price = ((old_items_average_price + new_items_average_price)) / (new_items + old_items)

        return round(average_price)


def set_new_captain(taverns):
    random_tavern = random.choice(taverns)
    random_tavern.captain = True

def text_separation():
    print("-" * 90)

def all_cities_change_turn(cities):
    for city in cities:
        city.change_turn()

def select_boat_from_convoy(convoy):
    counter = 1
    for boat in convoy.boats:
        print("{}- {}. ({}) {}% health.\n".
              format(counter, boat.name, boat.city.name, boat.health))
    option = input()
    option = correct_values(1, len(convoy.boats), option)
    return convoy.boats[option - 1]


# have to finish battle.
def boat_battle_who_starts(boat, pirate):
    who_starts = random.choice([boat, pirate])
    who_goes_after = 0
    if who_starts == boat:
        who_goes_after = pirate
    else:
        who_goes_after = boat
    return who_starts, who_goes_after


def boat_battle(who_starts, who_goes_after):
    while who_starts.health > 1 or who_goes_after.health > 1:
        who_goes_after.health -= who_starts.firepower
        print("{} fires at {} and made {} damage."
              .format(who_starts.name, who_goes_after.name, who_starts.firepower))
        who_starts.health -= who_goes_after.firepower
        print("{} fires at {} and made {} damage."
              .format(who_goes_after.name, who_starts.name, who_goes_after.firepower))
        print("{} health is {} and {} health is {}."
              .format(who_starts.name, who_starts.health, who_goes_after.name, who_goes_after.health))


def choose_boat_from_city(city):
    print("Is your ship free or in a convoy?\n"
          "1- Ship.\n"
          "2- Convoy.\n"
          "3- Exit.\n")
    option = input()
    option = correct_values(1, 3, option)
    if option == 3:
        return False
    elif option == 1:
        return choose_boat(city)
    elif option == 2:
        return choose_boat_from_convoy(city)

def choose_boat_or_convoy_from_city(city):
    print("Do you want to select a ship or a convoy?\n"
          "1- Ship.\n"
          "2- Convoy.\n"
          "3- Exit.\n")
    option = input()
    option = correct_values(1, 3, option)
    if option == 3:
        return False
    elif option == 1:
        return choose_boat(city), "boat"
    elif option == 2:
        return choose_convoy(city), "convoy"

def choose_boat(city):
    counter = 1
    for boat in city.boats:
        print("{}- {}.".format(counter, boat.name))
        counter += 1
    option = input()
    option = correct_values(1, len(city.boats), option)
    return city.boats[option - 1]

def choose_boat_from_convoy(city):
    counter = 1
    for convoy in city.convoys:
        print("{} {}".format(counter, convoy.name))
        counter += 1
    option = input()
    option = correct_values(1, len(city.convoys), option)
    return choose_boat(city.convoys[option - 1])

def choose_convoy(city):
    counter = 1
    for convoy in city.convoys:
        print("{} {}".format(counter, convoy.name))
        counter += 1
    option = input()
    option = correct_values(1, len(city.convoys), option)
    return city.convoys[option - 1]